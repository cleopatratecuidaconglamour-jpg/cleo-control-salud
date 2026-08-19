import os

from flask import Flask, jsonify, request, send_from_directory
from openai import OpenAI

app = Flask(__name__)
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))


@app.route("/")
def inicio():
    return send_from_directory(".", "index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True) or {}
    mensaje = str(data.get("message", "")).strip()

    if not mensaje:
        return jsonify({"error": "Escribe un mensaje."}), 400

    try:
        respuesta = client.responses.create(
            model="gpt-5-mini",
            instructions=(
                "Eres Cleo Control Salud, un asistente virtual educativo "
                "de apoyo para personas con hipertension y diabetes. "
                "Explica de forma clara, breve y segura. "
                "No diagnostiques, no cambies medicacion ni indiques dosis. "
                "Ante sintomas potencialmente graves, indica buscar atencion "
                "medica urgente. Recuerda que no sustituyes al equipo de salud."
            ),
            input=mensaje,
        )

        return jsonify({"reply": respuesta.output_text})

    except Exception:
        return jsonify(
            {"error": "No pude procesar la consulta en este momento."}
        ), 500


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
