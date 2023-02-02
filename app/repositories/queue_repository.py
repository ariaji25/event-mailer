import datetime
from typing import List


from app.config import Config
from app.database import db, orm
from app.utils import loger, date_time


class QUEUE_STATUS:
    PENDING = 0
    PROCESSED = 1
    FAILED = 2


class Queue(db.Entity):
    id = orm.PrimaryKey(int, auto=True)
    payload = orm.Required(orm.Json)
    status = orm.Optional(int, default=QUEUE_STATUS.PENDING)
    created_at = orm.Optional(
        datetime.datetime, default=date_time.get_datetime_now())
    updated_at = orm.Optional(datetime.datetime)


@orm.db_session
def create_queue_item(payload: orm.Json):
    new_entry = Queue(payload=payload, status=QUEUE_STATUS.PENDING)
    orm.commit()
    loger.log_info("Created Entry", new_entry.id,
                   new_entry.payload, new_entry.status)
    return new_entry.id

@orm.db_session
def create_bulk_queue_item(payloads: List[orm.Json]):
    queue_items = [Queue(payload=p, status=QUEUE_STATUS.PENDING) for p in payloads]
    orm.commit()
    return len(queue_items)



@orm.db_session
def get_pending_queue_items(limit: int =5):
    queue_items, err = [],''
    try:
        queue_items = Queue.select(lambda q: q.status == QUEUE_STATUS.PENDING).order_by(lambda q: q.created_at).limit(limit)[:]
        loger.log_info("Queue", queue_items)
    except:
        err='failed-get-queue'
    return queue_items, err

@orm.db_session
def update_queue_item_status(item_id: id, new_status: int):
    item = Queue[item_id]
    item.status = new_status
    item.updated_at = date_time.get_datetime_now()
    orm.commit()
    loger.log_info("Queue item updated ", item.id, item.status)
    return item
