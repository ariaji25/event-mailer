from app.models.audience_model import AudienceModel, GetAudienceParam
from app.usecases import audience_usecase
from app.utils import response_builder

def create_audience_controller(audience: AudienceModel):
    audience_id, err = audience_usecase.create_audience_usecase(audience=audience)
    if len(err) > 0 and err.lower().__contains__("notfound"):
        return response_builder.notfound_response(err)
    if len(err) > 0 and err.lower().__contains__("is-exist"):
        return response_builder.badrequest_response(err)
    if len(err) > 0:
        return response_builder.error_response()
    else:
        return response_builder.created_response(audience_id)

def get_audience_controller(param: GetAudienceParam):
    audiences, err = audience_usecase.get_audience_usecase(param)
    if len(err) > 0 and err.lower().__contains__("notfound"):
        return response_builder.notfound_response(err)
    if len(err) > 0:
        return response_builder.error_response()
    else:
        return response_builder.success_response(audiences)

