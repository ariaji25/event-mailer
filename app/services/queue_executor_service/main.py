import os
import sys
import time
from dotenv import load_dotenv
load_dotenv()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR.replace("/app/services", ""))

from app.utils import loger
from app.usecases import queue_usecase
from app.database import init_database_connection

def main():
    time.tzset()
    init_database_connection()
    loger.log_info("Queue executor started")
    queue_usecase.process_pending_queue_items_usecase()
    
main()