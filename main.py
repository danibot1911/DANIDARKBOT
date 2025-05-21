from flask import Flask, request
import requests
import datetime
import time

app = Flask(__name__)

# ==== CREDENCIALES INCORPORADAS ====
BOT_TOKEN = "7566801240:AAF-VrtRg4sexDFZ24azNz9AdpQc626xTnE"
CHAT_ID = "1454815028"
URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

# ==== FUNCIÓN PARA ENVIAR MENSAJES ====
def enviar_alerta_telegram(texto):
    if not BOT_TOKEN or not CHAT_ID:
        print("Token o Chat ID no configurado.")
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

# ==== SIMULACIÓN DE DETECCIÓN DE PATRONES ====
def detectar_patron_ruleta():
    ahora = datetime.datetime.now().strftime("%H:%M:%S")
    patron_detectado = True
    mensaje = f"<b>DanyDarkBot activada</b>\nHora: {ahora}\n\n<b>Patrón detectado en ruleta</b>\nPosibilidad de acierto: <b>ALTA</b>\n\nActúa rápido, amor"
    
    if patron_detectado:
        enviar_alerta_telegram(mensaje)

# ==== ENDPOINT PRINCIPAL PARA TEST ====
@app.route('/', methods=['GET'])
def index():
    detectar_patron_ruleta()
    return "DanyDarkBot en línea."

# ==== EJECUCIÓN DEL SISTEMA ====
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
