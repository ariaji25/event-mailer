from flask import Flask
from flask_pydantic import validate

from app.models import *
from app.controllers import *
from app.main import app

# Register Events API
@app.route("/api/events", methods=["POST"])
@validate()
def create_event(body: EventModel):
    return create_event_controller(body)


@app.route("/api/events", methods=["GET"])
@validate()
def get_events(query: GetEventParams):
    return get_events_controller(query)


# Audiences endpoint
@app.route("/api/audiences", methods=['POST'])
@validate()
def create_audiences(body: AudienceModel):
    return create_audience_controller(body)

@app.route("/api/audiences", methods=['GET'])
@validate()
def get_audiences(query: GetAudienceParam):
    return get_audience_controller(query)

# Email endpoint
@app.route("/api/save_emails", methods=['POST'])
@validate()
def create_scheduled_email(body: EmailModel):
    return email_controller.create_scheduled_email_controller(body)

@app.route("/api/emails", methods=['GET'])
@validate()
def get_scheduled_email(query: GetEmailParam):
    return email_controller.get_scheduled_email_controller(query)

