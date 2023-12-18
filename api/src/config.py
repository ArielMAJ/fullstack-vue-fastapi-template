"""
Application's and its environment's configuration.
"""

import os


class Config:
    """Base configuration."""

    ENVIRONMENT = os.getenv("ENVIRONMENT", "DEV")
    DEBUG = ENVIRONMENT == "DEV"
    TESTING = ENVIRONMENT == "TEST"

    HOST = os.getenv("APPLICATION_HOST", "127.0.0.1")
    PORT = int(os.getenv("APPLICATION_PORT", "3000"))

    APPLICATION_ROOT = os.getenv("APPLICATION_ROOT", "")


class TestConfig(Config):
    """Test configuration."""

    ENVIRONMENT = "TEST"
    TESTING = True
    DEBUG = False
    PRESERVE_CONTEXT_ON_EXCEPTION = False
