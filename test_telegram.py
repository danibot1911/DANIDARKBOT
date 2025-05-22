import requests

BOT_TOKEN = "7566801240:AAF-VrtRg4sexDFZ..."  # Pon aquí tu token real
CHAT_ID = "1454815028"
MENSAJE = "<b>DanyDarkBot activada</b>\nHora: 12:34:56\n<b>Patrón detectado en ruleta</b>\nPosibilidad de acierto: <b>ALTA</b>\nActúa rápido, amor"

def enviar_mensaje():
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": MENSAJE,
        "parse_mode": "HTML"
    }
    response = requests.post(url, data=data)
    if response.status_code == 200:
        print("Mensaje enviado correctamente")
    else:
        print("Fallo al enviar:", response.text)

enviar_mensaje()
