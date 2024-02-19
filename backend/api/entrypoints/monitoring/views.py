from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def health_check() -> None:
    """
    Checks the health of the project.

    It returns 200 if the project is healthy.
    """
