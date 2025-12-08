from .base import AppException

class ServiceError(AppException):
    pass
class ValidationError(AppException):
    pass