from api.entrypoints.v1.random_number.schema import RandomResponse
from api.services.random_number_service import RandomNumberService
from api.utils.custom_decorators import cache
from fastapi import APIRouter

router = APIRouter()


@router.get("/", response_model=RandomResponse)
@cache(expire=5)
async def random_number():
    """
    Sends random number back to user.

    :returns: random number to user.
    """
    return await RandomNumberService.get_random_number()
