import pytest
from api.app import get_app
from fastapi.testclient import TestClient


@pytest.fixture(scope="function")
def client():
    """Create a TestClient instance for testing."""
    return TestClient(get_app())
