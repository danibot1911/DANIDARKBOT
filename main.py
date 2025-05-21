from flask import Flask, request
import requests
import datetime
import asyncio
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
    import asyncio
from rushbet_acceso_automatizado import obtener_numeros_ruleta
from utils.telegram_mejorado_pi import enviar_mensaje_telegram
import time

# ID de tu chat o grupo
CHAT_ID = "1454815028"  # Asegúrate que este sea correcto

# Lista de patrones conocidos (puedes expandirla)
PATRONES_VALIDOS = [
    [8, 11, 10],
    [0, 8, 20],
    [21, 18, 16],
    [32, 0, 5],
]

def analizar_patron(numeros):
    if len(numeros) >= 3:
        ultimos = numeros[-3:]
        return ultimos in PATRONES_VALIDOS
    return False

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
                    mensaje = f"DANI DARK ALERTA:\nPatrón detectado: {numeros[-3:]}\nEnlace: https://www.rushbet.co/?page=all-games&game=225"
                    await enviar_mensaje_telegram(mensaje, CHAT_ID)
        except Exception as e:
            print(f"Error en monitoreo: {e}")
        await asyncio.sleep(15)  # Revisa cada 15 segundos

# Lanzar la tarea en segundo plano
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(ciclo_monitoreo())
    loop.run_forever()
    
    
    app.run(host='0.0.0.0', port=10000)
