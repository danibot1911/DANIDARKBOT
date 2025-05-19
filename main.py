from flask import Flask, request
from utils.analizador_ruleta import analizar_patron_ruleta
from config import TELEGRAM_TOKEN, TELEGRAM_CHAT_ID
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return "S3T RULETA OPERATIVA – LISTA PARA CAZAR"

@app.route('/alerta', methods=['POST', 'GET'])
def recibir_resultado():
    if request.method == 'POST':
        data = request.json
    else:  # GET desde navegador
        resultados_str = request.args.get("resultados", "")
        secuencia = [int(n) for n in resultados_str.split(",") if n.isdigit()]
        data = {"resultados": secuencia}
    
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
import os
app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
