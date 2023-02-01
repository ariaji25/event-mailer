from pydantic import BaseModel
import datetime
from typing import Optional, List

from .base_response_model import BaseResponseModel

class EventModel(BaseModel):
    id: Optional[int]
    event_name: str
    event_date: datetime.datetime

class GetEventParams(BaseModel):
    page: Optional[int] = 1
    
