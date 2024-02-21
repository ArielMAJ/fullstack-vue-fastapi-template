from api.config import Config, TestConfig
from fastapi_cache.decorator import cache as fastapi_cache


def ignore_cache(func):
    return func


def cache(*args, **kwargs):
    if Config.ENVIRONMENT == TestConfig.ENVIRONMENT:
        return ignore_cache
    return fastapi_cache(*args, **kwargs)
