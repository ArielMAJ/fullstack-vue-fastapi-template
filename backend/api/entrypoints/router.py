from fastapi.routing import APIRouter

from api.entrypoints import monitoring, v1

api_router = APIRouter()
api_router.include_router(monitoring.router)
api_router.include_router(v1.router, prefix="/v1", tags=["v1"])
