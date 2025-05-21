from flask import Flask, request
import requests
import datetime
import asyncio
from rushbet_acceso_automatizado import obtener_numeros_ruleta

# ==== CONFIGURACIÓN MANUAL ====
BOT_TOKEN = "7566801240:AAf-VrtRg4sexDFZ24az..."  # Reemplaza por tu token real completo si falta
CHAT_ID = "1454815028"
URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

app = Flask(__name__)

# ==== FUNCIÓN PARA ENVIAR MENSAJE A TELEGRAM ====
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

# ==== LISTA DE PATRONES CONOCIDOS ====
PATRONES_VALIDOS = [
    [8, 11, 10],
    [0, 8, 20],
    [21, 18, 16],
    [32, 0, 5]
]

# ==== ANÁLISIS DE PATRONES ====
def analizar_patron(numeros):
    if len(numeros) >= 3:
        ultimos = numeros[-3:]
        return ultimos in PATRONES_VALIDOS
    return False

# ==== CICLO DE MONITOREO ====
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
                    mensaje = f"<b>DANY DARK ALERTA</b>\n"
                    mensaje += f"<b>Patrón detectado:</b> {numeros[-3:]}\n"
                    mensaje += f"Posibilidad de acierto: <b>ALTA</b>\n"
                    mensaje += f"Actúa rápido, amor"
                    await asyncio.to_thread(enviar_alerta_telegram, mensaje)

        except Exception as e:
            print(f"Error en monitoreo: {e}")

        await asyncio.sleep(15)

# ==== INICIO AUTOMÁTICO ====
if __name__ == "__main__":
    print("==> DanyDarkBot corriendo en puerto 10000")
    loop = asyncio.get_event_loop()
    loop.create_task(ciclo_monitoreo())
    loop.run_forever()
    app.run(host="0.0.0.0", port=10000, debug=True)
    
