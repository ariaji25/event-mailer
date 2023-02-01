import time
import os, sys


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)


from usecases import email_usecase, queue_usecase
from utils import loger
from database import init_database_connection



def start_cron_service():
    pending_emails = email_usecase.get_pending_email_uesecase()
    if len(pending_emails) > 0:
        loger.log_info("Adding emails to queue", len(pending_emails), "to queue")
        for e in pending_emails:
            queue_usecase.add_queue_item_usecase(email=e)
    time.sleep(60)
    start_cron_service()

init_database_connection()
time.sleep(3)
loger.log_info("Cron service start")
start_cron_service()

    
