from .base import AppException

class repository_exceptions(AppException):
    pass

class NotFoundError(repository_exceptions):
    def __init__(self, entity_name: str, entity_id: int):
        super().__init__(f"{entity_name} with id {entity_id} not found")
