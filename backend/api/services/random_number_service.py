"""
Random number service class.
"""


import asyncio

import random
from loguru import logger
from api.entrypoints.v1.random_number.schema import RandomResponse


class RandomNumberService:
    """
    Random number service class.
    """

    @staticmethod
    async def get_random_number() -> RandomResponse:
        """
        Get random number.

        :returns: random number.
        """
        seconds = random.random() * 5
        logger.debug(f"Sleeping for {seconds} seconds before answering request.")
        await asyncio.sleep(seconds)
        return RandomResponse(message=round(seconds, 2))