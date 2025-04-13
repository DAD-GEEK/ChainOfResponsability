from handlers.base_handler import BaseHandler
from models.request_model import RequestModel

class AuthHandler(BaseHandler):
    def handle(self, request: RequestModel) -> bool:
        if request.credentials != "token_valido":
            return False
        return super().handle(request)
