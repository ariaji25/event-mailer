import datetime

from app.database import db, orm
from . import Event
from app.utils import loger
from app.config import Config

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
    audiences_id, err = 0, ''
    try:
        event = Event[event_id]
        new_audience = Audience(
            event_id=event,
            name=name,
            email=email
        )
        orm.commit()
        audiences_id = new_audience.id
        loger.log_info(new_audience.id, new_audience.name, new_audience.email)
    except:
        err='failed-save-audience'
    return audiences_id, err

@orm.db_session
def get_audience_by_event_id(event_id: int, page: int = 1):
    audiences, err = [],''
    try:
        audiences = Audience.select(lambda a: a.event_id.id == event_id).page(page)[:]
    except:    
        err='failed-get-audience'
    loger.log_info(audiences,err)
    return audiences, err

@orm.db_session
def is_exist(email:str,event_id:int):
    audiences = Audience.select(lambda a: a.email == email and a.event_id.id == event_id)[:]
    return len(audiences) > 0


