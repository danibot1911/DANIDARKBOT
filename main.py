import requests
import asyncio
import datetime
from flask import Flask
from bs4 import BeautifulSoup

# ====== CONFIGURACIÓN TELEGRAM ======
BOT_TOKEN = "7566801240:AAF-VrtRg4sexDFZ..."  # Reemplaza por tu token real
CHAT_ID = "1454815028"

# ====== CONFIGURACIÓN RUSHBET ======
RUSHBET_RULETA_URL = "https://www.rushbet.co/?page=casino&game=external/roulette"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X)"
}

# ====== FLASK APP ======
app = Flask(__name__)

# ====== PATRONES CONOCIDOS ======
PATRONES_VALIDOS = [
    [8, 11, 10],
    [0, 8, 20],
    [21, 18, 16],
    [32, 0, 5]
]

# ====== ENVÍO A TELEGRAM ======
def enviar_mensaje_telegram(mensaje):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": mensaje,
        "parse_mode": "HTML"
    }
    try:
        response = requests.post(url, data=data)
        if response.status_code == 200:
            print("[TELEGRAM] Enviado correctamente")
        else:
            print(f"[TELEGRAM] Falló: {response.text}")
    except Exception as e:
        print(f"[TELEGRAM] Error de conexión: {e}")

# ====== OBTENER NÚMEROS DE RULETA ======
def obtener_numeros_ruleta():
    try:
        response = requests.get(RUSHBET_RULETA_URL, headers=HEADERS)
        soup = BeautifulSoup(response.content, "html.parser")
        numeros = []

        for span in soup.find_all("span"):
            texto = span.get_text().strip()
            if texto.isdigit():
                num = int(texto)
                if 0 <= num <= 36:
                    numeros.append(num)

        if numeros:
            print(f"[RUSHBET] Números capturados: {numeros}")
            return numeros
        else:
            print("[RUSHBET] No se detectaron números")
            return []

    except Exception as e:
        print(f"[ERROR] Obteniendo números de ruleta: {e}")
        return []

# ====== DETECTOR DE PATRÓN ======
def analizar_patron(numeros):
    if len(numeros) >= 3:
        ultimos = numeros[-3:]
        return ultimos in PATRONES_VALIDOS
    return False

# ====== CICLO DE MONITOREO ======
async def ciclo_monitor():
    historial = []
    print("[BOT] Iniciando monitoreo...")

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

        await asyncio.sleep(15)

# ====== ENDPOINT PING ======
@app.route('/', methods=['GET'])
def index():
    return "DanyDarkBot en línea."

# ====== INICIO DEL BOT ======
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(ciclo_monitor())
    loop.run_forever()
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port, debug=True)
