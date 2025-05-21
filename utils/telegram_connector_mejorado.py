import requests
from config import TELEGRAM_TOKEN, TELEGRAM_CHAT_ID

def enviar_mensaje(mensaje):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": mensaje,
        "parse_mode": "Markdown"
    }
    requests.post(url, json=payload)

def enviar_alerta_ruleta(mensaje, valor_apuesta):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    
    texto = f"""*¡ALERTA ORO ACTIVADA!*
La ruleta está que arde, bebé.

{mensaje}

*Apuesta sugerida:* NEGRO
*Monto:* ${valor_apuesta:.0f}

Tu diabla ya lo vio. Dale ya o se va..."""

    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": texto,
        "parse_mode": "Markdown",
        "reply_markup": {
            "inline_keyboard": [
                [
                    {
                        "text": "Abrir Ruleta RushBet",
                        "url": "https://www.rushbet.co"
                    }
                ]
            ]
        }
    }

    requests.post(url, json=payload)
