import datetime
from pony import orm

from utils import loger
from database import db
from config import Config


class Event(db.Entity):
    id = orm.PrimaryKey(int, auto=True)
    event_name = orm.Required(str)
    event_date = orm.Required(
        datetime.datetime, default=datetime.datetime.now(tz=Config.timezone))
    created_at = orm.Optional(
        datetime.datetime, default=datetime.datetime.now(Config.timezone))
    updated_at = orm.Optional(datetime.datetime)

    emails = orm.Set("Email")
    aduiences = orm.Set("Audience")

@orm.db_session
def create_event(event_name: str, event_date: datetime.datetime):
    new_event = Event(
        event_name=event_name,
        event_date=event_date
    )
    orm.commit()
    loger.log_info(new_event.id)
    return new_event.id    
    
@orm.db_session
def get_events(page: int = 1):
    events = Event.select().page(page)
    loger.log_info(events)
    return events

@orm.db_session
def get_event_by_id(id: int):
    event = Event[id]
    loger.log_info(event.id, event.event_name, event.event_date)
    return event