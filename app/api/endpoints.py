from flask import Flask
from flask_pydantic import validate

from app.models import *
from app.controllers import *
from app import app

# Register Events API
@app.route("/api/events", methods=["POST"])
@validate()
def create_event(body: EventModel):
    return create_event_controller(body)


@app.route("/api/events", methods=["GET"])
@validate()
def get_events(query: GetEventParams):
    return get_events_controller(query)