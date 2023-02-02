from typing import List

from app.repositories import *
from app.utils import loger, date_time
from app.models import EmailModel, GetEmailParam


def email_to_email_model(email: Email) -> EmailModel:
    return EmailModel(
        id=email.id,
        email_subject=email.email_subject,
        email_content=email.email_content,
        event_id=email.event_id.id,
        timestamp=email.timestamp
    )


def get_pending_email_uesecase():
    datetime_now = date_time.get_datetime_now()
    after = datetime_now - datetime.timedelta(minutes=1)
    before = datetime_now + datetime.timedelta(minutes=1)
    loger.log_info("Get email after-{} before-{}".format(after, before))
    emails = email_repository.get_emails(after=after, before=before)
    loger.log_info("Emails ", emails)
    return emails


def create_scheduled_email_usecase(email: EmailModel) -> tuple[int, str]:
    event_exist = event_repository.is_exist(email.event_id)
    if not event_exist:
        return 0, 'event-{}-notfound'.format(email.event_id)

    email_id, err = email_repository.create_email(
        event_id=email.event_id,
        email_subject=email.email_subject,
        email_content=email.email_content,
        email_schedule=email.timestamp
    )
    return email_id, err


def get_scheduled_email_usecase(param: GetEmailParam) -> tuple[List[EmailModel], str]:
    event_exist = event_repository.is_exist(param.event_id)
    if not event_exist:
        return 0, 'event-{}-notfound'.format(param.event_id)

    emails, err = email_repository.get_emails_by_event_id(
        param.event_id, param.page)
    if len(emails) > 0:
        emails = [email_to_email_model(e) for e in emails]
    return emails, err
