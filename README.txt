# Cleo Control Salud — Módulo 6 IA

Este prototipo contiene:

- `index.html`: app móvil.
- `server.py`: backend que protege la clave API.
- `requirements.txt`: dependencias.

## Para ejecutar

1. Crear una API key de OpenAI.
2. Guardarla como variable de entorno `OPENAI_API_KEY`. No escribirla dentro de `index.html`.
3. Instalar dependencias:
   `pip install -r requirements.txt`
4. Ejecutar:
   `python server.py`
5. Abrir en navegador:
   `http://localhost:8000`

Para publicarla y usarla desde un celular fuera de la computadora, hay que desplegar este servidor en un hosting HTTPS.

## Importante

Es un prototipo educativo, no un dispositivo médico ni un sustituto de la atención profesional.
Antes de usarlo con pacientes reales se necesita revisar privacidad, consentimiento, seguridad, normativa de datos de salud, evaluación clínica y procedimientos de emergencia.
