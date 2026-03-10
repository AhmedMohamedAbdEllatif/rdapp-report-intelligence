from pathlib import Path

import pytest

from app.config import Settings


REQUIRED_ENV_VARS = (
    "MAX_CONCURRENT_JOBS",
    "LLM_MAX_CALLS",
    "LLM_TIMEOUT",
    "STORAGE_PATH",
    "CACHE_DIR",
    "EXTRACTOR_VERSION",
)


@pytest.fixture(autouse=True)
def clear_settings_env(monkeypatch: pytest.MonkeyPatch) -> None:
    for env_var in REQUIRED_ENV_VARS:
        monkeypatch.delenv(env_var, raising=False)


def test_settings_use_defaults() -> None:
    settings = Settings(_env_file=None)

    assert settings.MAX_CONCURRENT_JOBS == 4
    assert settings.LLM_MAX_CALLS == 10
    assert settings.LLM_TIMEOUT == 60
    assert settings.STORAGE_PATH == Path("storage")
    assert settings.CACHE_DIR == Path(".cache")
    assert settings.EXTRACTOR_VERSION == "v1"


def test_settings_load_from_environment_variables(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    monkeypatch.setenv("MAX_CONCURRENT_JOBS", "8")
    monkeypatch.setenv("LLM_MAX_CALLS", "25")
    monkeypatch.setenv("LLM_TIMEOUT", "120")
    monkeypatch.setenv("STORAGE_PATH", str(tmp_path / "storage"))
    monkeypatch.setenv("CACHE_DIR", str(tmp_path / "cache"))
    monkeypatch.setenv("EXTRACTOR_VERSION", "v2")

    settings = Settings(_env_file=None)

    assert settings.MAX_CONCURRENT_JOBS == 8
    assert settings.LLM_MAX_CALLS == 25
    assert settings.LLM_TIMEOUT == 120
    assert settings.STORAGE_PATH == tmp_path / "storage"
    assert settings.CACHE_DIR == tmp_path / "cache"
    assert settings.EXTRACTOR_VERSION == "v2"


def test_settings_load_from_dotenv_file(tmp_path: Path) -> None:
    env_file = tmp_path / ".env"
    env_file.write_text(
        "\n".join(
            [
                "MAX_CONCURRENT_JOBS=2",
                "LLM_MAX_CALLS=5",
                "LLM_TIMEOUT=30",
                f"STORAGE_PATH={tmp_path / 'data'}",
                f"CACHE_DIR={tmp_path / 'cache-dir'}",
                "EXTRACTOR_VERSION=v3",
            ]
        ),
        encoding="utf-8",
    )

    settings = Settings(_env_file=env_file)

    assert settings.MAX_CONCURRENT_JOBS == 2
    assert settings.LLM_MAX_CALLS == 5
    assert settings.LLM_TIMEOUT == 30
    assert settings.STORAGE_PATH == tmp_path / "data"
    assert settings.CACHE_DIR == tmp_path / "cache-dir"
    assert settings.EXTRACTOR_VERSION == "v3"
