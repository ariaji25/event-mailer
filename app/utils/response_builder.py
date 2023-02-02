from app.models.base_response_model import BaseResponseModel, BaseModel
from flask_api import status


def success_response(data):
    response = BaseResponseModel(
        message="OK",
        error=False,
        status=status.HTTP_200_OK,
    )
    response.data = data
    return response, response.status


def created_response(data):
    response = BaseResponseModel(
        message="Success",
        error=False,
        status=status.HTTP_201_CREATED,
    )
    response.data = data
    return response, status.HTTP_201_CREATED

def notfound_response(message):
    response = BaseResponseModel(
        message="Data notfound [{}]".format(message),
        error=True,
        status=status.HTTP_404_NOT_FOUND,
    )
    return response, response.status

def badrequest_response(message):
    response = BaseResponseModel(
        message="Bad Request [{}]".format(message),
        error=True,
        status=status.HTTP_400_BAD_REQUEST,
    )
    return response, response.status

def error_response():
    response = BaseResponseModel(
        message="Server error",
        error=True,
        status=status.HTTP_500_INTERNAL_SERVER_ERROR,
    )
    return response, response.status
