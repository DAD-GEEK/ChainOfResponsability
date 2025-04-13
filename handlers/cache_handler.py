from handlers.base_handler import BaseHandler
from models.request_model import RequestModel


class CacheHandler(BaseHandler):
    cache = {}

    def handle(self, request: RequestModel) -> bool:
        key = str(request.data)
        if key in self.cache:
            return True
        self.cache[key] = "respuesta_guardada"
        return super().handle(request)
