from abc import ABC, abstractmethod
from models.request_model import RequestModel


class BaseHandler(ABC):
    _next = None

    def set_next(self, handler: 'BaseHandler') -> 'BaseHandler':
        self._next = handler
        return handler

    @abstractmethod
    def handle(self, request: RequestModel) -> bool:
        if self._next:
            return self._next.handle(request)
        return True
