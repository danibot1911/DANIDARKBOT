import time
from utils.analizador_ruleta import analizar_patron_ruleta
from config import TELEGRAM_TOKEN, TELEGRAM_CHAT_ID
import requests

# Simulación de resultados de ruleta en vivo (puedes reemplazar por scraping real más adelante)
ruleta_simulada = [
    [7, 23, 5, 9, 27, 3, 1],    # 6 rojos
    [2, 4, 6, 8, 10, 13, 15],   # 6 negros
    [17, 18, 19, 20, 21, 22, 23],
    [32, 19, 7, 18, 25, 36, 27]
]

def enviar_alerta_telegram(texto):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": f"**ALERTA S3T RULETA – MODO ORO ACTIVADO**\n\n{texto}",
        "parse_mode": "Markdown"
    }
    requests.post(url, json=payload)

def modo_oro_activo():
    print(">> MODO ORO INICIADO – ESCANEANDO CADA 10s")

    while True:
        secuencia = ruleta_simulada[int(time.time()) % len(ruleta_simulada)]
        mensaje = analizar_patron_ruleta(secuencia)
        if mensaje:
            enviar_alerta_telegram(mensaje)
        time.sleep(10)
