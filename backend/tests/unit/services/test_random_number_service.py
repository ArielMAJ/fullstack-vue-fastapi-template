"""Unit tests for the random number service."""

import pytest


from api.services.random_number_service import RandomNumberService
from api.entrypoints.v1.random_number.schema import RandomResponse

@pytest.mark.asyncio
@pytest.mark.parametrize("random_return_value", [0.1, 0.2, 0.3])  # Specify different sleep times here
async def test_root_response_GET(client, mocker, random_return_value):
    """Test the endpoint."""
    mock_sleep = mocker.patch("asyncio.sleep")
    mock_sleep.side_effect = lambda *args, **kwargs: None

    mock_random = mocker.patch("random.random")
    mock_random.return_value = random_return_value

    response = await RandomNumberService.get_random_number()
    
    assert isinstance(response, RandomResponse)
    assert response == RandomResponse(message=random_return_value * 5)
    assert response.message == random_return_value * 5
    mock_sleep.assert_called_once_with(random_return_value * 5)
