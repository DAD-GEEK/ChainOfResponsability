from models.request_model import RequestModel
from handlers.auth_handler import AuthHandler
from handlers.data_validator_handler import DataValidatorHandler
from handlers.brute_force_handler import BruteForceHandler
from handlers.cache_handler import CacheHandler

class OrderClientService:
    def __init__(self):
        self.chain = self.build_chain()

    def build_chain(self):
        auth = AuthHandler()
        validator = DataValidatorHandler()
        brute = BruteForceHandler()
        cache = CacheHandler()

        auth.set_next(validator).set_next(brute).set_next(cache)
        return auth

    def process_request(self, request: RequestModel) -> bool:
        return self.chain.handle(request)
