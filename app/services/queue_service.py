import time
import os, sys


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from src.use_cases import queue_usecase
from database import init_database_connection
from utils import loger

def queue_service():
    finish = queue_usecase.process_pending_queue_items_usecase()
    if finish:
        time.sleep(1)
        queue_service()

init_database_connection()
loger.log_info("Queue service started")
queue_service()