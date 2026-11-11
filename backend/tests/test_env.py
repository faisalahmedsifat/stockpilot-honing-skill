from app.core.config import Settings


def test_settings_load_from_environment(monkeypatch):
    monkeypatch.setenv("APP_NAME", "StockPilot Staging")
    monkeypatch.setenv("APP_ENV", "testing")
    monkeypatch.setenv("DEBUG", "true")

    settings = Settings()

    assert settings.app_name == "StockPilot Staging"
    assert settings.app_env == "testing"
    assert settings.debug is True
