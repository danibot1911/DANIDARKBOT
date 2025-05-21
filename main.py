from flask import Flask, request
import requests
import datetime
import asyncio

from rushbet_acceso_automatizado import obtener_numeros_ruleta
from telegram_mejorado_pi import enviar_mensaje_telegram

# ==== CONFIGURACIÓN ====
BOT_TOKEN = "7566801240:AA...Z4az"  # Usa el tuyo si aún no está arriba
CHAT_ID = "1454815028"
URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

app = Flask(__name__)

# ==== PATRONES CONOCIDOS ====
PATRONES_VALIDOS = [
    [8, 11, 10],
    [0, 8, 20],
    [21, 18, 16],
    [32, 0, 5],
]

# ==== DETECTOR DE PATRÓN ====
def analizar_patron(numeros):
    if len(numeros) >= 3:
        ultimos = numeros[-3:]
        return ultimos in PATRONES_VALIDOS
    return False

# ==== CICLO MONITOREO ====
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
                    mensaje = (
                        "<b>DANY DARK ALERTA ACTIVADA</b>\n"
                        "Patrón detectado en ruleta\n"
                        "<b>Posibilidad de acierto:</b> ALTA\n"
                        "Actúa rápido, amor"
                    )
                    await enviar_mensaje_telegram(mensaje)
        except Exception as e:
            print(f"Error en monitoreo: {e}")

        await asyncio.sleep(15)  # Revisión cada 15 segundos

# ==== RUTA PRINCIPAL (ping de prueba) ====
@app.route('/', methods=['GET'])
def index():
    return "DanyDarkBot en línea."

# ==== INICIO AUTOMÁTICO ====
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(ciclo_monitoreo())
    loop.run_forever()

    print("==> DanyDarkBot corriendo en puerto 10000")
    app.run(host='0.0.0.0', port=10000, debug=True)
    
