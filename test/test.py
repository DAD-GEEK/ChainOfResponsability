from models.request_model import RequestModel
from services.order_client_service import OrderClientService

def prueba_proceso_solicitudes():
    client = OrderClientService()

    solicitudes = [
        # Credenciales incorrectas
        RequestModel(credentials="invalido", data={"producto": "libro"}, ip="192.168.1.1"),

        # Solicitud válida
        RequestModel(credentials="token_valido", data={"producto": "libro"}, ip="192.168.1.2"),

        # Cache activa (mismo data)
        RequestModel(credentials="token_valido", data={"producto": "libro"}, ip="192.168.1.3"),

        # Fuerza bruta simulada
        RequestModel(credentials="invalido", data={"producto": "mouse"}, ip="192.168.1.10"),
        RequestModel(credentials="invalido", data={"producto": "mouse"}, ip="192.168.1.10"),
        RequestModel(credentials="invalido", data={"producto": "mouse"}, ip="192.168.1.10"),
        RequestModel(credentials="invalido", data={"producto": "mouse"}, ip="192.168.1.10"),
        RequestModel(credentials="invalido", data={"producto": "mouse"}, ip="192.168.1.10"),

        # Solicitud válida pero IP ya bloqueada
        RequestModel(credentials="token_valido", data={"producto": "mouse"}, ip="192.168.1.10"),
    ]

    for i, req in enumerate(solicitudes, 1):
        print(f"\n----- Solicitud #{i} desde IP {req.ip} -----")
        resultado = client.process_request(req)
        print("Resultado:", "Aceptada" if resultado else "Rechazada")

if __name__ == "__main__":
    prueba_proceso_solicitudes()
