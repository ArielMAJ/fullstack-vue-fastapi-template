from pydantic import BaseModel


class RootResponse(BaseModel):
    message: str
