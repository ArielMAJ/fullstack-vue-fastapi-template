"""End-to-end test for the health endpoint."""


def test_health(client):
    """Test the health endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() is None
