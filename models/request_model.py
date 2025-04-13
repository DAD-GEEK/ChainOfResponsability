from pydantic import BaseModel
from typing import Dict

class RequestModel(BaseModel):
    credentials: str
    data: Dict
    ip: str