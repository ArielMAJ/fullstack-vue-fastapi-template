import pytest
from api.utils.custom_decorators import cache, ignore_cache


@pytest.mark.parametrize(
    "environment, expected, not_expected",
    [
        ("test", ignore_cache, 1),
        ("dev", 1, ignore_cache),
        ("prd", 1, ignore_cache),
    ],
)
def test_cache(mocker, environment, expected, not_expected):
    mock_config = mocker.patch("api.utils.custom_decorators.Config")
    mock_config.ENVIRONMENT = environment

    mock_fastapi_cache = mocker.patch("api.utils.custom_decorators.fastapi_cache")
    mock_fastapi_cache.return_value = 1

    assert cache() == expected
    assert cache() != not_expected
