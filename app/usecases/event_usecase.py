from typing import List

from app.models import EventModel
from app.repositories import event_repository, Event


def event_to_event_model(event: Event) -> EventModel:
    return EventModel(id=event.id, event_name=event.event_name, event_date=event.event_date)

def create_event_usecase(event: EventModel) -> tuple[int, str]:
    new_event, err = event_repository.create_event(
        event_name=event.event_name, event_date=event.event_date)
    return new_event, err


def get_event_usecase(page: int) -> tuple[List[EventModel], str]:
    events, err = event_repository.get_events(page)
    if len(events) > 0:
        events = [event_to_event_model(e) for e in events]
    return events, err
