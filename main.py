from flask import Flask, request, jsonify
from utils.telegram_connector_mejorado import enviar_mensaje_telegram
from utils.analizador_ruleta import analizar_secuencia
import os

app = Flask(__name__)

# Carga el token y chat_id desde variables de entorno
TOKEN_BOT = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

@app.route("/", methods=["GET"])
def index():
    return "DanyDarkBot está vivo y listo para cazar ruleta."

@app.route("/a", methods=["POST"])
def recibir_secuencia():
    try:
        data = request.json
        secuencia = data.get("secuencia", [])
        
        if not secuencia or not isinstance(secuencia, list):
            return jsonify({"error": "Secuencia inválida"}), 400

        mensaje_analisis = analizar_secuencia(secuencia)

        if mensaje_analisis:
            enviar_mensaje_telegram(mensaje_analisis)
            return jsonify({"mensaje": "Alerta enviada", "secuencia": secuencia}), 200
        else:
            return jsonify({"mensaje": "Secuencia sin patrones relevantes"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

import threading
from utils.modo_ruleta_sombra import modo_ruleta_sombra

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
