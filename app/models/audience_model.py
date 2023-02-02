from pydantic import BaseModel
from typing import Optional


class AudienceModel(BaseModel):
    id: Optional[int]
    name: str
    email: str
    event_id: int


class GetAudienceParam(BaseModel):
    event_id: int
    page: Optional[int] = 1
