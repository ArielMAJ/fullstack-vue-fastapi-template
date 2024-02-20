"""Unit tests for the root endpoint service."""

import pytest
from api.entrypoints.v1.root_response.schema import RootResponse
from api.services.root_response_service import RootResponseService


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "random_return_value", [0.1, 0.2, 0.3]
)  # Specify different sleep times here
async def test_root_response_service(mocker, random_return_value):
    """Test the endpoint."""
    mock_sleep = mocker.patch("asyncio.sleep")
    mock_sleep.side_effect = lambda *args, **kwargs: None

    mock_random = mocker.patch("api.services.root_response_service.random")
    mock_random.return_value = random_return_value

    response = await RootResponseService.get_root_response()

    assert isinstance(response, RootResponse)
    assert response == RootResponse(message="Hello World message from the back-end!")
    assert response.message == "Hello World message from the back-end!"
    mock_sleep.assert_called_once_with(random_return_value * 7)
