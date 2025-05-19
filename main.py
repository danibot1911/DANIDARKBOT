from flask import Flask, request
from utils.analizador_ruleta import analizar_patron_ruleta
import config

app = Flask(__name__)

@app.route('/')
def index():
    return "OPERACIÓN S3T RULETA – ONLINE"

@app.route('/alerta', methods=['POST'])
def recibir_resultado():
    data = request.json
    secuencia = data.get("resultados")  # Lista de números tipo [23, 17, 36, 19, 32]
    alerta = analizar_patron_ruleta(secuencia)
    if alerta:
        # Aquí conectar con Telegram
        print("ALERTA:", alerta)
    return {"status": "ok"}, 200

if __name__ == "__main__":
    app.run()
