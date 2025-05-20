import requests
from config import TELEGRAM_TOKEN, TELEGRAM_CHAT_ID

def enviar_mensaje(mensaje):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": mensaje,
        "parse_mode": "Markdown"
    }
    response = requests.post(url, json=data)
    print("Respuesta Telegram:", response.status_code, response.text)
    return response.status_code
