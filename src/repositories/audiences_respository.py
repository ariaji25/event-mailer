import datetime

from database import db, orm
from . import Event
from utils import loger
from config import Config

class Audience(db.Entity):
    id=orm.PrimaryKey(int, auto=True)
    event_id=orm.Required(Event)
    name=orm.Required(str)
    email=orm.Required(str)
    created_at = orm.Optional(
        datetime.datetime, default=datetime.datetime.now(Config.timezone))
    updated_at = orm.Optional(datetime.datetime)



@orm.db_session
def create_audience(event_id: int, name: str, email: str):
    event = Event[event_id]
    new_audience = Audience(
        event_id=event,
        name=name,
        email=email
    )
    orm.commit()
    loger.log_info(new_audience.id, new_audience.name, new_audience.email)
    return new_audience

@orm.db_session
def get_audience_by_event_id(event_id: int):
    audiences = Audience.select(lambda a: a.event_id.id == event_id)[:]
    loger.log_info(audiences[0].name)
    return audiences

