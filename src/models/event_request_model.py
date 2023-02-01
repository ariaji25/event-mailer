from pydantic import BaseModel
import datetime

class EventModel(BaseModel):
    event_name: str
    event_date: datetime.datetime