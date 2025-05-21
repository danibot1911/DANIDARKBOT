from flask import Flask, request
from utils.analizador_ruleta import analizar_patron_ruleta
from utils.valor_sugerido import calcular_valor_apuesta
from config import TELEGRAM_TOKEN, TELEGRAM_CHAT_ID
from utils.telegram_connector_mejorado import enviar_mensaje
from loop_oro import modo_oro_activo
from modo_sniper_asistido import detectar_sniper_asistido
import requests
import os
from threading import Thread

app = Flask(__name__)

@app.route("/", methods=["POST"])
def index():
    return "S3T RULETA — ONLINE"

@app.route('/alerta', methods=['POST', 'GET'])
def recibir_resultado():
    if request.method == 'POST':
        data = request.json
        mensaje = "¡ALERTA S3T RULETA – MODO ORO ACTIVADO!\nSe detectaron 7 números ROJOS en las últimas 7 jugadas.\nRecomendación: Apostar NEGRO."
        enviar_mensaje(mensaje)
    else:
        resultados_str = request.args.get("resultados", "")
        secuencia = [int(n) for n in resultados_str.split(",")]
        data = {"resultados": secuencia}

    secuencia = data.get("resultados", [])
    mensaje = analizar_patron_ruleta(secuencia)
    if mensaje:
        enviar_alerta_telegram(mensaje)
    return {"status": "procesado"}, 200

def enviar_alerta_telegram(texto):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": f"**ALERTA S3T RULETA**\n\n{texto}",
        "parse_mode": "Markdown"
    }
    requests.post(url, json=payload)

@app.route("/oro", methods=['GET'])
def activar_oro():
    Thread(target=modo_oro_activo).start()
    return "MODO ORO ACTIVADO"

@app.route("/sniper", methods=["POST"])
def sniper():
    try:
        datos = request.get_json()
        mensaje = datos.get("mensaje", "").lower()
        secuencia = datos.get("secuencia", [])
        respuesta = detectar_sniper_asistido(mensaje, secuencia)
        return respuesta, 200
    except Exception as e:
        return {"error": str(e)}, 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
