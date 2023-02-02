import os
import sys
import time, sched
from dotenv import load_dotenv
load_dotenv()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR.replace("/app/services", ""))

from app.utils import loger
from app.usecases import queue_usecase
from app.database import init_database_connection

def process_queue():
    time.tzset()
    loger.log_info("Queue executor started")
    queue_usecase.process_pending_queue_items_usecase()

def start_process(scheduler): 
    # do schedule for the next call
    scheduler.enter(5, 1, start_process, (scheduler,))
    process_queue()

def main():
    init_database_connection()
    my_scheduler = sched.scheduler(time.time, time.sleep)
    my_scheduler.enter(5, 1, start_process, (my_scheduler,))
    my_scheduler.run()

main()
