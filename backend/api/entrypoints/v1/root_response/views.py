
from fastapi import APIRouter

from api.entrypoints.v1.root_response.schema import RootResponse

from api.services.root_response_service import RootResponseService


router = APIRouter()




@router.get("/", response_model=RootResponse)
async def root():
    """
    Sends root response back to user.

    :returns: root response to user.
    """
    return await RootResponseService.get_root_response()