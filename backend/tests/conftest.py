import pytest
from fastapi.testclient import TestClient
from api.app import get_app

@pytest.fixture
def client():
    """Create a TestClient instance for testing."""
    return TestClient(get_app())
