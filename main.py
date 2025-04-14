from fastapi import FastAPI, HTTPException
from models.request_model import RequestModel
from services.order_client_service import OrderClientService

app = FastAPI()
client_service = OrderClientService()

@app.post("/ordenes")
def crear_orden(request: RequestModel):
    if client_service.process_request(request):
        return {"message": "Orden procesada exitosamente"}
    else:
        raise HTTPException(status_code=403, detail="Solicitud rechazada")
