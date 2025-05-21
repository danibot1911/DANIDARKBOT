from flask import Flask, request
import requests
import os
import datetime

app = Flask(__name__)

# ===== CONFIG =====
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

# ===== FUNCIONES BASE =====
def enviar_alerta_telegram(texto):
    if not BOT_TOKEN or not CHAT_ID:
        print("Token o Chat ID no configurado")
        return

    data = {
        "chat_id": CHAT_ID,
        "text": texto,
        "parse_mode": "HTML"
    }

    try:
        response = requests.post(URL, data=data)
        if response.status_code != 200:
            print("Error al enviar mensaje:", response.text)
        else:
            print("Mensaje enviado correctamente.")
    except Exception as e:
        print("Error al conectar con Telegram:", e)


# ===== SIMULACIÓN DE ANÁLISIS RULETA =====
def detectar_patron_ruleta():
    # Aquí puedes integrar más adelante tu lógica real
    ahora = datetime.datetime.now().strftime("%H:%M:%S")
    patron_detectado = True  # Simulación de que encontró patrón
    mensaje = f"<b>DanyDarkBot activada</b>\nHora: {ahora}\n\n<b>Patrón detectado en ruleta</b>\nPosibilidad de acierto: <b>ALTA</b>\n\n<b>Actúa rápido, amor</b>"

    if patron_detectado:
        enviar_alerta_telegram(mensaje)


# ===== ENDPOINT PRINCIPAL (PING) =====
@app.route('/', methods=['GET'])
def index():
    detectar_patron_ruleta()
    return "DanyDarkBot en línea."


# ===== PUNTO DE INICIO =====
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
