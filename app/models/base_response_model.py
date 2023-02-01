from pydantic import BaseModel
from typing import Optional


class BaseResponseModel(BaseModel):
    message: str
    error: bool
    status: int
    data = ''
