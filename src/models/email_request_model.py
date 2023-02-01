from pydantic import BaseModel
import datetime


class EmailRequestModel(BaseModel):
    event_id: int
    email_subject: str
    email_content: str
    timestamp: datetime.datetime
