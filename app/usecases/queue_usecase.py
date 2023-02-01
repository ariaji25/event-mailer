from typing import List
import time

from app.repositories import queue_repository, email_repository, event_repository, audiences_respository, orm
from app.utils import loger
from app.services import email_service


def add_queue_item_usecase(email: email_repository.Email):
    event: event_repository.Event = email.event_id
    recepients: List[audiences_respository.Audience] = [
        a.email for a in audiences_respository.get_audience_by_event_id(event_id=event.id)]
    data: orm.Json = {
        "subject": email.email_subject,
        "body": email.email_content,
        "recepients": recepients
    }
    item = queue_repository.create_queue_item(payload=data)
    return item


def process_queue_item_usecase(item: queue_repository.Queue):
    loger.log_info("Process queue ", item.id, item.payload)
    email_service.send_email(item.payload)
    updated_item = queue_repository.update_queue_item_status(
        item.id, queue_repository.QUEUE_STATUS.PROCESSED)
    return updated_item


def process_pending_queue_items_usecase():
    items: List[queue_repository.Queue] = queue_repository.get_pending_queue_items(limit=1)
    if len(items) > 0:
        loger.log_info("Will Process ", items[0].id, " queue items")
        result = process_queue_item_usecase(items[0])
        loger.log_info("Process result ", result.id, result.status)
        time.sleep(1)
    else:
        loger.log_info("Empty queue")
    return True
