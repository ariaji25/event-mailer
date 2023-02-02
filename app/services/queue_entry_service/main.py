
import sys
import os
import time
from dotenv import load_dotenv
load_dotenv()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR.replace("/app/services", ""))

from app.utils import loger
from app.usecases import email_usecase, queue_usecase
from app.database import init_database_connection
from app.services import email_service

def main():
    time.tzset()
    init_database_connection()
    loger.log_info("Queue entry started")
    pending_emails = email_usecase.get_pending_email_uesecase()
    if len(pending_emails) > 0:
        loger.log_info("Adding emails to queue",
                       len(pending_emails), "to queue")
        for e in pending_emails:
            queue_usecase.add_queue_item_usecase(email=e)


main()