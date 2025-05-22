# main.py

from flask import Flask, request
import requests
import datetime
import asyncio
from rushbet_acceso_automatizado import obtener_numeros_ruleta
from utils.telegram_mejorado_pi import enviar_mensaje_telegram

# === CONFIGURACIÓN ===
BOT_TOKEN = "7566801240:AAF-VrtRg4sexDFZ24azNz9AdpQc626xTnE"
CHAT_ID = "1454815028"
URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

app = Flask(__name__)

# === PATRONES CONOCIDOS ===
PATRONES_VALIDOS = [
    [8, 11, 10],
    [0, 8, 20],
    [21, 18, 16],
    [32, 0, 5],
]

# === DETECTOR DE PATRÓN ===
def analizar_patron(numeros):
    if len(numeros) >= 3:
        ultimos = numeros[-3:]
        return ultimos in PATRONES_VALIDOS
    return False

# === CICLO MONITOREO ===
async def ciclo_monitoreo():
    print("Iniciando monitoreo de ruleta...")
    historial = []

    while True:
        try:
            numeros = obtener_numeros_ruleta()
            print(f"Números detectados: {numeros}")

            if numeros != historial:
                historial = numeros

                if analizar_patron(numeros):
                    hora = datetime.datetime.now().strftime("%H:%M:%S")
                    mensaje = (
                        f"<b>DanyDarkBot activada</b>\n"
                        f"Hora: {hora}\n\n"
                        f"<b>Patrón detectado en ruleta</b>\n"
                        f"Posibilidad de acierto: <b>ALTA</b>\n\n"
                        f"Actúa rápido, amor"
                    )
                    await enviar_mensaje_telegram(BOT_TOKEN, CHAT_ID, mensaje)
        except Exception as e:
            print(f"Error en monitoreo: {e}")

        await asyncio.sleep(15)  # Espera entre ciclos

# === RUTA PRINCIPAL ===
@app.route('/', methods=['GET'])
def index():
    return "DanyDarkBot está viva."

# === RUTA PARA RECIBIR MENSAJES DE TELEGRAM ===
@app.route(f"/{BOT_TOKEN}", methods=["POST"])
def recibir_update():
    data = request.get_json()
    print(f"[UPDATE] {data}")
    return {"ok": True}

# === INICIO AUTOMÁTICO ===
if __name__ == "__main__":
    import os

    loop = asyncio.get_event_loop()
    loop.create_task(ciclo_monitoreo())
    loop.run_forever()

    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

