from typing import List

from app.repositories import *
from app.utils import loger, date_time
from app.database import orm


def get_pending_email_uesecase():
  datetime_now = date_time.get_datetime_now()
  after = datetime_now - datetime.timedelta(minutes=1)
  before = datetime_now + datetime.timedelta(minutes=1)
  emails = email_repository.get_emails(after=after, before=before)
  loger.log_info("Emails ", emails)
  return emails