import requests
import asyncio
import datetime
import threading
from flask import Flask
from bs4 import BeautifulSoup
from utils.telegram_mejorado_pi import enviar_mensaje_telegram
import os

# ===== CONFIGURACIÓN =====
BOT_TOKEN = "7566801240:AAF-VrtRg4sexDFZ24azNz9AdpQc626xTnE"
CHAT_ID = "1454815028"

RUSHBET_RULETA_URL = "https://www.rushbet.co/?page=casino&game=external/roulette"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X)"
}
PATRONES_VALIDOS = [[8, 11, 10], [0, 8, 20], [21, 18, 16], [32, 0, 5]]

# ===== FLASK =====
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "DanyDarkBot en línea."

# ===== TELEGRAM =====
def enviar_mensaje_telegram(mensaje):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": mensaje, "parse_mode": "HTML"}
    try:
        response = requests.post(url, data=data)
        print(f"[TELEGRAM] Código: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"[ERROR TELEGRAM] {e}")

# ===== RUSHBET =====
def obtener_numeros_ruleta():
    try:
        response = requests.get(RUSHBET_RULETA_URL, headers=HEADERS)
        soup = BeautifulSoup(response.content, "html.parser")
        numeros = []
        for span in soup.find_all("span"):
            texto = span.get_text().strip()
            if texto.isdigit():
                n = int(texto)
                if 0 <= n <= 36:
                    numeros.append(n)
        return numeros
    except Exception as e:
        print(f"[ERROR RUSHBET] {e}")
        return []

def analizar_patron(numeros):
    if len(numeros) >= 3:
        ultimos = numeros[-3:]
        return ultimos in PATRONES_VALIDOS
    return False

# ===== MONITOREO EN HILO =====
def iniciar_monitoreo():
    historial = []
    while True:
        numeros = obtener_numeros_ruleta()
        if numeros != historial:
            historial = numeros
            if analizar_patron(numeros):
                hora = datetime.datetime.now().strftime("%H:%M:%S")
                mensaje = (
                    f"<b>DanyDarkBot activada</b>\n"
                    f"Hora: {hora}\n"
                    f"<b>Patrón detectado en ruleta</b>\n"
                    f"Posibilidad de acierto: <b>ALTA</b>\n"
                    f"Actúa rápido, amor"
                )
                enviar_mensaje_telegram(mensaje)
        asyncio.run(asyncio.sleep(15))

# ===== MAIN =====
if __name__ == '__main__':
    threading.Thread(target=iniciar_monitoreo, daemon=True).start()
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
