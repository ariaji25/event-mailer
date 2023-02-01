from app.models.event_model import EventModel, GetEventParams
from app.usecases.event_usecase import *
from app.utils import response_builder


def create_event_controller(event: EventModel):
    new_event_id, err = create_event_usecase(event=event)
    if len(err) > 0:
        return response_builder.error_response()
    else:
        return response_builder.created_response(new_event_id)

def get_events_controller(param: GetEventParams):
    events, err = get_event_usecase(param.page)
    if len(err) > 0:
        return response_builder.error_response()
    else:
        return response_builder.success_response(events)