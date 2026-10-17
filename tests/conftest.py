import pytest


@pytest.fixture(autouse=True)
def no_real_api_key(monkeypatch):
    # Tests must never call the real API, even if the developer has a key loaded.
    monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)
