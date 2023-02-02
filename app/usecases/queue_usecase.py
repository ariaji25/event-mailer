from typing import List
import time

from app.repositories import queue_repository, email_repository, event_repository, audiences_respository, orm
from app.utils import loger
from app.services import email_service


def add_queue_item_usecase(email: email_repository.Email):
    event: event_repository.Event = email.event_id
    email_repository.update_email(email.id)
    audiences, _ = audiences_respository.get_audience_by_event_id(
        event_id=event.id)
    recepients: List[audiences_respository.Audience] = [
        a.email for a in audiences]
    data: orm.Json = {
        "subject": email.email_subject,
        "body": email.email_content,
        "recepients": recepients
    }
    item = queue_repository.create_queue_item(payload=data)
    return item


def process_queue_item_usecase(item: queue_repository.Queue):
    loger.log_info("Process queue ", item.id, item.payload)

    def on_finish(success):
        queue_repository.update_queue_item_status(
            item.id, (queue_repository.QUEUE_STATUS.PROCESSED if success else queue_repository.QUEUE_STATUS.FAILED))

    email_service.send_email(item.payload, func=on_finish)


def process_pending_queue_items_usecase():
    items, err = queue_repository.get_pending_queue_items(
        limit=1)
    if len(items) > 0 and len(err) <= 0:
        loger.log_info("Will Process ", items[0].id, " queue item")
        process_queue_item_usecase(items[0])
    else:
        loger.log_info("Empty queue")
    return True
