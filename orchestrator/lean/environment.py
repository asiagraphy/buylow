"""LEAN 프로세스를 띄우기 위한 런타임 환경 해석.

uv 프로젝트의 Python 3.11과 잠긴 의존성을 백테스트·라이브에서 함께 사용한다.
.NET·공유 라이브러리·AlgorithmImports 경로 해석과 런처 빌드를 담당한다.
"""

from __future__ import annotations

import os
import shutil
import subprocess
import sys
import sysconfig
from dataclasses import dataclass
from pathlib import Path

# net10 호환 LEAN NuGet 계보. semver상 더 큰 10730.x는 net462라 금지 (docs/DEVELOPMENT.md).
LEAN_PKG_VERSION = "2.5.17757"

# orchestrator/lean/environment.py → parents[2] = repo 루트
REPO_ROOT = Path(__file__).resolve().parents[2]
LAUNCHER_CSPROJ = REPO_ROOT / "launcher" / "BuylowLauncher.csproj"
LAUNCHER_OUT = REPO_ROOT / "launcher" / "bin" / "Release" / "net10.0"


@dataclass(frozen=True)
class LeanEnvironment:
    """LEAN 프로세스 spawn에 필요한, 해석이 끝난 경로 묶음."""

    dotnet_exe: Path
    dotnet_root: Path
    pythonnet_pydll: Path        # pythonnet이 로드할 libpython (PYTHONNET_PYDLL)
    venv_site_packages: Path     # pandas/numpy 깐 3.11 venv의 site-packages
    algorithm_imports_dir: Path  # 'from AlgorithmImports import *' 해소용 디렉토리
    launcher_dll: Path           # 빌드된 BuylowLauncher.dll

    def process_env(self, pythonpath_parts: list[str]) -> dict[str, str]:
        """LEAN 프로세스에 넘길 환경변수(os.environ + .NET/pythonnet 설정)."""
        env = dict(os.environ)
        env["DOTNET_ROOT"] = str(self.dotnet_root)
        env["PATH"] = f"{self.dotnet_root}{os.pathsep}{env.get('PATH', '')}"
        env["DOTNET_CLI_TELEMETRY_OPTOUT"] = "1"
        env["PYTHONNET_PYDLL"] = str(self.pythonnet_pydll)
        env["PYTHONPATH"] = os.pathsep.join(pythonpath_parts)
        return env


def _libpython_filename(platform: str = sys.platform) -> str:
    """플랫폼별 libpython 3.11 공유 라이브러리 파일명. (테스트용으로 platform 인자 주입 가능)"""
    if platform == "darwin":
        return "libpython3.11.dylib"
    if platform.startswith("linux"):
        return "libpython3.11.so"
    if platform == "win32":
        # Windows는 메이저·마이너만 붙은 DLL (예: python311.dll), lib 접두사·점 없음.
        return "python311.dll"
    raise RuntimeError(f"지원하지 않는 플랫폼: {platform}")


def _dotnet_exe_name(platform: str = sys.platform) -> str:
    return "dotnet.exe" if platform == "win32" else "dotnet"


def _resolve_dotnet() -> tuple[Path, Path]:
    """(dotnet 실행파일, DOTNET_ROOT)를 해석. 기본 위치는 ~/.dotnet."""
    dotnet_root = Path(os.environ.get("DOTNET_ROOT", Path.home() / ".dotnet"))
    candidate = dotnet_root / _dotnet_exe_name()
    if candidate.exists():
        return candidate, dotnet_root
    # PATH에 있으면 그걸 사용 (Windows는 winget이 PATH에 dotnet.exe 등록)
    on_path = shutil.which("dotnet")
    if on_path:
        exe = Path(on_path).resolve()
        return exe, exe.parent
    raise RuntimeError("dotnet을 찾을 수 없음. .NET 10 SDK 설치 필요 (docs/DEVELOPMENT.md)")


def _resolve_pythonnet_pydll() -> Path:
    """uv가 선택한 인터프리터와 동일한 공유 라이브러리를 사용한다."""
    if sys.version_info[:2] != (3, 11):
        raise RuntimeError("LEAN은 Python 3.11이 필요합니다. uv sync --locked 후 uv run으로 실행하세요.")
    if sys.platform == "win32":
        pydll = Path(sys.base_prefix) / _libpython_filename(sys.platform)
    else:
        library = sysconfig.get_config_var("LDLIBRARY") or _libpython_filename(sys.platform)
        pydll = Path(sysconfig.get_config_var("LIBDIR") or sys.base_prefix) / library
    if not pydll.is_file():
        raise RuntimeError("Python 3.11 공유 라이브러리가 없습니다. uv python install 3.11 후 uv sync --locked를 실행하세요.")
    return pydll


def _project_site_packages() -> Path:
    """LEAN에도 uv.lock에서 설치한 동일 의존성을 전달한다."""
    import numpy
    import pandas

    return Path(sysconfig.get_path("purelib"))


def _build_launcher(dotnet_exe: Path, dotnet_root: Path) -> Path:
    """thin 런처를 빌드(=NuGet 복원 포함)하고 산출 DLL 경로 반환."""
    env = dict(os.environ)
    env["DOTNET_ROOT"] = str(dotnet_root)
    env["DOTNET_CLI_TELEMETRY_OPTOUT"] = "1"
    print(">> 런처 빌드")
    subprocess.run(
        [str(dotnet_exe), "build", str(LAUNCHER_CSPROJ), "-c", "Release", "--nologo", "-v", "quiet"],
        check=True, env=env,
    )
    dll = LAUNCHER_OUT / "BuylowLauncher.dll"
    if not dll.exists():
        raise RuntimeError(f"빌드 후 런처 DLL이 없음: {dll}")
    return dll


def _resolve_algorithm_imports() -> Path:
    """AlgorithmImports.py가 든 디렉토리(QuantConnect.Common NuGet의 content/)."""
    ai_dir = (
        Path(os.environ.get("NUGET_PACKAGES") or Path.home() / ".nuget" / "packages") / "quantconnect.common"
        / LEAN_PKG_VERSION / "content"
    )
    if not (ai_dir / "AlgorithmImports.py").exists():
        raise RuntimeError(f"AlgorithmImports.py를 찾을 수 없음: {ai_dir} (런처 빌드 필요)")
    return ai_dir


def prepare_environment() -> LeanEnvironment:
    """LEAN 실행에 필요한 모든 경로를 해석/준비한다.

    순서 주의: 런처 빌드가 NuGet을 복원하므로, AlgorithmImports 해석은 빌드 이후에 한다.
    """
    dotnet_exe, dotnet_root = _resolve_dotnet()
    pydll = _resolve_pythonnet_pydll()
    site_packages = _project_site_packages()
    launcher_dll = _build_launcher(dotnet_exe, dotnet_root)
    ai_dir = _resolve_algorithm_imports()
    return LeanEnvironment(
        dotnet_exe=dotnet_exe,
        dotnet_root=dotnet_root,
        pythonnet_pydll=pydll,
        venv_site_packages=site_packages,
        algorithm_imports_dir=ai_dir,
        launcher_dll=launcher_dll,
    )
