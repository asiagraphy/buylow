"""uv 프로젝트 인터프리터와 LEAN 공유 라이브러리의 일치 검증."""

from pathlib import Path

import pytest

from orchestrator.lean import environment as env


# ── 플랫폼별 순수 매핑 ────────────────────────────────────────────────────────
def test_libpython_filename_per_platform():
    assert env._libpython_filename("darwin") == "libpython3.11.dylib"
    assert env._libpython_filename("linux") == "libpython3.11.so"
    assert env._libpython_filename("win32") == "python311.dll"


def test_libpython_filename_unknown_platform_raises():
    with pytest.raises(RuntimeError):
        env._libpython_filename("plan9")


def test_dotnet_exe_name_per_platform():
    assert env._dotnet_exe_name("win32") == "dotnet.exe"
    assert env._dotnet_exe_name("darwin") == "dotnet"
    assert env._dotnet_exe_name("linux") == "dotnet"


def test_shared_library_uses_windows_base_interpreter(tmp_path, monkeypatch):
    library = tmp_path / "python311.dll"
    library.touch()
    monkeypatch.setattr(env.sys, "platform", "win32")
    monkeypatch.setattr(env.sys, "base_prefix", str(tmp_path))
    assert env._resolve_pythonnet_pydll() == library


def test_shared_library_uses_current_interpreter_sysconfig(tmp_path, monkeypatch):
    library = tmp_path / "libpython3.11.so.1.0"
    library.touch()
    monkeypatch.setattr(env.sys, "platform", "linux")
    variables = {"LIBDIR": str(tmp_path), "LDLIBRARY": library.name}
    monkeypatch.setattr(env.sysconfig, "get_config_var", variables.get)
    monkeypatch.setattr(env.shutil, "which", lambda name: None)
    assert env._resolve_pythonnet_pydll() == library


def test_shared_library_rejects_wrong_python(monkeypatch):
    monkeypatch.setattr(env.sys, "version_info", (3, 12, 0))
    with pytest.raises(RuntimeError, match="uv run"):
        env._resolve_pythonnet_pydll()


def test_missing_shared_library_fails_before_launch(tmp_path, monkeypatch):
    monkeypatch.setattr(env.sys, "platform", "win32")
    monkeypatch.setattr(env.sys, "base_prefix", str(tmp_path))
    with pytest.raises(RuntimeError, match="공유 라이브러리"):
        env._resolve_pythonnet_pydll()


def test_lean_uses_project_dependencies():
    import numpy
    import pandas

    packages = env._project_site_packages().resolve()
    assert Path(numpy.__file__).resolve().is_relative_to(packages)
    assert Path(pandas.__file__).resolve().is_relative_to(packages)


def test_algorithm_imports_honors_nuget_packages(tmp_path, monkeypatch):
    content = tmp_path / "quantconnect.common" / env.LEAN_PKG_VERSION / "content"
    content.mkdir(parents=True)
    (content / "AlgorithmImports.py").touch()
    monkeypatch.setenv("NUGET_PACKAGES", str(tmp_path))
    assert env._resolve_algorithm_imports() == content


# ── 현재 OS에서의 실제 해석(integration) ──────────────────────────────────────
@pytest.mark.integration
def test_resolve_pythonnet_pydll_on_this_os():
    # 개발 머신(3.11 설치돼 있어야)에서 실제 libpython 경로가 잡히는지.
    pydll = env._resolve_pythonnet_pydll()
    assert pydll.exists()
    import ctypes

    assert ctypes.PyDLL(str(pydll)) is not None
