from handlers.base_handler import BaseHandler
from models.request_model import RequestModel


class BruteForceHandler(BaseHandler):
    failed_ips = {}

    def handle(self, request: RequestModel) -> bool:
        if self.failed_ips.get(request.ip, 0) >= 5:
            return False
        return super().handle(request)
