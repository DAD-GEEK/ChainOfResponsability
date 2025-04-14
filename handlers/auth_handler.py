from handlers.base_handler import BaseHandler
from models.request_model import RequestModel
from handlers.brute_force_handler import BruteForceHandler  
bruteForceHandler = BruteForceHandler()

class AuthHandler(BaseHandler):
    def handle(self, request: RequestModel) -> bool:
        if request.credentials != "token_valido":
            print("Credenciales inválidas")
            bruteForceHandler.add_failed_ip(request.ip)
            return False
        return super().handle(request)
