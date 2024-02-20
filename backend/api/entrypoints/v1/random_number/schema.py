from pydantic import BaseModel


class RandomResponse(BaseModel):
    """Random response model."""

    message: float
