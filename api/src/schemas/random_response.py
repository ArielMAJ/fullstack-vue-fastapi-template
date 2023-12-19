from pydantic import BaseModel


class RandomResponse(BaseModel):
    message: float
