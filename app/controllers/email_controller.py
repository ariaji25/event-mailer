from app.models import EmailModel, GetEmailParam
from app.usecases import email_usecase
from app.utils import response_builder

def create_scheduled_email_controller(email: EmailModel):
    email_id, err = email_usecase.create_scheduled_email_usecase(email=email)
    if len(err) > 0 and err.lower().__contains__("notfound"):
        return response_builder.notfound_response(err)
    if len(err) > 0:
        return response_builder.error_response()
    else:
        return response_builder.created_response(email_id)
  
def get_scheduled_email_controller(param: GetEmailParam):
    emails, err = email_usecase.get_scheduled_email_usecase(param)
    if len(err) > 0 and err.lower().__contains__("notfound"):
        return response_builder.notfound_response(err)
    if len(err) > 0:
        return response_builder.error_response()
    else:
        return response_builder.success_response(emails)