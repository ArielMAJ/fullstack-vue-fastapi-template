"""End-to-end tests for the v1 root endpoint GET method."""

import pytest


@pytest.mark.parametrize(
    "random_return_value", [0.1, 0.2, 0.3]
)  # Specify different sleep times here
def test_root_response_GET(client, mocker, random_return_value):
    """Test the endpoint."""
    mock_sleep = mocker.patch("asyncio.sleep")
    mock_sleep.side_effect = lambda *args, **kwargs: None

    mock_random = mocker.patch("api.services.random_number_service.random")
    mock_random.return_value = random_return_value

    response = client.get("/v1/random_number/")
    assert response.status_code == 200
    assert response.json() == {"message": random_return_value * 5}
    mock_sleep.assert_called_once_with(random_return_value * 5)
