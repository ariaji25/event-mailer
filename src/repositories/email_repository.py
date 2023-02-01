import datetime

from database import db, orm
from . import Event
from utils import loger
from config import Config

class Email(db.Entity):
    id=orm.PrimaryKey(int, auto=True)
    event_id=orm.Required(Event)
    email_subject=orm.Required(str)
    email_content=orm.Required(str)
    timestamp=orm.Required(datetime.datetime)
    created_at = orm.Optional(
        datetime.datetime, default=datetime.datetime.now(Config.timezone))
    updated_at = orm.Optional(datetime.datetime)

    

@orm.db_session
def create_email(event_id:int, email_subject: str, email_content:str, email_schedule: datetime.datetime):
    event = Event[event_id]
    new_email = Email(
        event_id=event,
        email_subject=email_subject,
        email_content=email_content,
        timestamp=email_schedule
    )
    orm.commit()
    loger.log_info(new_email.id, new_email.email_subject, new_email.timestamp)
    return new_email

@orm.db_session
def get_emails(after: datetime.datetime, before: datetime.datetime):
    emails = Email.select(lambda e: e.timestamp < before and e.timestamp > after).order_by(lambda e: e.created_at)[:]
    return emails
            