# ChainOfResponsability

Este proyecto implementa el patrón de diseño **Chain of Responsibility** en Python. El objetivo es procesar solicitudes a través de una cadena de manejadores, donde cada manejador decide si procesa la solicitud o la pasa al siguiente.

## Estructura del Proyecto

- **`main.py`**: Punto de entrada de la aplicación.
- **`handlers/`**: Contiene los manejadores que forman la cadena.
- **`models/`**: Define los modelos de datos utilizados en el proyecto.
- **`services/`**: Contiene la lógica para construir y ejecutar la cadena de manejadores.
- **`test/test.py`**: Script de prueba para validar el comportamiento de la cadena.

## Pruebas

Para probar el flujo de procesamiento de solicitudes, ejecuta el script `test.py`:

```bash
python test/test.py
```

Este script simula diferentes escenarios de solicitudes, como:

- Credenciales inválidas.
- Solicitudes válidas.
- Solicitudes repetidas (cacheadas).
- Ataques de fuerza bruta.
- Solicitudes desde IPs bloqueadas.
- El resultado de cada solicitud se imprimirá en la consola, indicando si fue Aceptada o Rechazada.


## Colección de Postman

Se incluye una colección de Postman para probar las solicitudes de la API. Puedes encontrarla en la carpeta `documents` con el nombre `ChainOfResponsibility.postman_collection.json`.

### Instrucciones para usar la colección:
1. Abre Postman.
2. Ve a **File > Import** y selecciona el archivo `ChainOfResponsibility.postman_collection.json`.
3. La colección aparecerá en Postman con las solicitudes configuradas para probar los diferentes escenarios.


## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Para más detalles, consulta el archivo [LICENSE](./LICENSE).