import requests
from config import TELEGRAM_TOKEN, TELEGRAM_CHAT_ID

def enviar_alerta_ruleta(mensaje, valor_apuesta=10000):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"

    texto = f"""*¡ALERTA S3T RULETA – MODO ORO ACTIVADO!*\n
{mensaje}

*Recomendación:* Apostar NEGRO.
*Monto sugerido:* ${valor_apuesta:,}"""

    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": texto,
        "parse_mode": "Markdown",
        "reply_markup": {
            "inline_keyboard": [
                [
                    {
                        "text": "Abrir Ruleta en RushBet",
                        "url": "https://www.rushbet.co/?page=all-games&game=225"
                    }
                ]
            ]
        }
    }

    response = requests.post(url, json=payload)
    return response.status_code
