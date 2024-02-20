"""
Root response service class.
"""

import asyncio
from random import random

from api.entrypoints.v1.root_response.schema import RootResponse
from loguru import logger


class RootResponseService:
    """
    Root response service class.
    """

    @staticmethod
    async def get_root_response() -> RootResponse:
        """
        Get root response.

        :returns: root response.
        """
        seconds = random() * 7
        logger.debug(f"Sleeping for {seconds} seconds before answering request.")
        await asyncio.sleep(seconds)
        return RootResponse(message="Hello World message from the back-end!")
