
from handlers.base_handler import BaseHandler
from models.request_model import RequestModel


class DataSanitizerHandler(BaseHandler):
    def handle(self, request: RequestModel) -> bool:
        # Validaciones de seguridad, tipos de datos, etc.
        return super().handle(request)
