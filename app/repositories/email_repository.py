import datetime

from app.database import db, orm
from . import Event
from app.utils import loger, date_time
from app.config import Config


class Email(db.Entity):
    id = orm.PrimaryKey(int, auto=True)
    event_id = orm.Required(Event)
    email_subject = orm.Required(str)
    email_content = orm.Required(str)
    timestamp = orm.Required(datetime.datetime)
    created_at = orm.Optional(
        datetime.datetime, default=datetime.datetime.now(Config.timezone))
    updated_at = orm.Optional(datetime.datetime)


@orm.db_session
def create_email(event_id: int, email_subject: str, email_content: str, email_schedule: datetime.datetime):
    email_id, err = 0, ''
    try:
        event = Event[event_id]
        new_email = Email(
            event_id=event,
            email_subject=email_subject,
            email_content=email_content,
            timestamp=email_schedule
        )
        orm.commit()
        loger.log_info(new_email.id, new_email.email_subject,
                       new_email.timestamp)
        email_id = new_email.id
    except:
        err = 'failed-save-email'
    return email_id, err


@orm.db_session
def get_emails(after: datetime.datetime, before: datetime.datetime):
    emails = Email.select(lambda e: e.timestamp < before and e.timestamp > after and e.updated_at is None).order_by(
        lambda e: e.created_at)[:]
    return emails

@orm.db_session
def get_emails_by_event_id(event_id: int, page: int):
    emails, err = [],''
    try:
        emails = Email.select(lambda e: e.event_id.id == event_id).page(page)[:]
    except:
        err="failed-get-email"
    return emails, err

@orm.db_session
def update_email(id:int):
    email=Email[id]
    email.updated_at = date_time.get_datetime_now()
    orm.commit()