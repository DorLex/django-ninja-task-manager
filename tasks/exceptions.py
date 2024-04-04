from ninja_extra import status
from ninja_extra.exceptions import APIException


class CustomException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'CustomException'
