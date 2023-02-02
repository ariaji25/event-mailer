from pydantic import BaseModel
import datetime
from typing import Optional


class EmailModel(BaseModel):
    id: Optional[int]
    event_id: int
    email_subject: str
    email_content: str
    timestamp: datetime.datetime

class GetEmailParam(BaseModel):
    page: Optional[int] = 1
    event_id: int
