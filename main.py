from flask import Flask, request
import requests
import datetime
from rushbet_acceso_automatizado import obtener_numeros_ruleta

# ===== CONFIGURACIÓN MANUAL =====
BOT_TOKEN = "7566801240:AAF-VrtRg4sexDFZ24azNz9AdpQc626xTnE"
CHAT_ID = "1454815028"
URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

app = Flask(__name__)

# ===== FUNCIÓN PARA ENVIAR MENSAJE A TELEGRAM =====
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
            print("Mensaje enviado correctamente")
    except Exception as e:
        print("Error al conectar con Telegram:", str(e))

# ===== ANÁLISIS DE PATRONES =====
def analizar_patrones(secuencia):
    patrones = []
    for i in range(len(secuencia) - 1):
        if secuencia[i + 1] - secuencia[i] == 2:
            patrones.append([secuencia[i], secuencia[i + 1]])
    return patrones

# ===== DETECCIÓN DE RULETA =====
def detectar_patron_ruleta():
    ahora = datetime.datetime.now().strftime("%H:%M:%S")
    secuencia = obtener_numeros_ruleta()

    if not secuencia:
        print("No se pudo obtener secuencia")
        return

    patrones_detectados = analizar_patrones(secuencia)

    if patrones_detectados:
        mensaje = f"<b>DanyDarkBot activada</b>\nHora: {ahora}\n\n"
        mensaje += "<b>Patrón detectado en ruleta</b>\n"
        mensaje += "Posibilidad de acierto: <b>ALTA</b>\n\n"
        mensaje += "Actúa rápido, amor"

        enviar_alerta_telegram(mensaje)
    else:
        print("No se detectaron patrones esta vez.")

# ===== ENDPOINT PRINCIPAL =====
@app.route('/', methods=['GET'])
def index():
    detectar_patron_ruleta()
    return "DanyDarkBot en línea."

# ===== INICIO AUTOMÁTICO =====
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
