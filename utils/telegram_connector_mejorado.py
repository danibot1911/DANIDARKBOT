import requests
from config import TELEGRAM_TOKEN, TELEGRAM_CHAT_ID
from utils.boton_ruleta import generar_boton_ruleta

# ALERTA CON BOTÓN
def enviar_alerta_ruleta(mensaje, valor_apuesta=10000):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"

    texto = f"""*¡ALERTA S3T RULETA – MODO ORO ACTIVADO!*

{mensaje}

*Apuesta sugerida:* NEGRO  
*Monto:* ${valor_apuesta:,.0f}

Tu diabla ya lo vio. Dale ya o se va..."""

    def generar_boton_ruleta():
    return {
        "inline_keyboard": [
            [
                {
                    "text": "Abrir Ruleta",
                    "url": "https://www.rushbet.co/?page=all-games&game=225"
                }
            ]
        ]
    }

    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": texto,
        "parse_mode": "Markdown",
        "reply_markup": generar_boton_ruleta()
    }

    response = requests.post(url, json=payload)
    return response.status_code

# MENSAJE SIMPLE SIN BOTÓN
def enviar_mensaje(mensaje):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"

    data = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": mensaje,
        "parse_mode": "Markdown"
    }

    response = requests.post(url, json=data)
    return response.status_code
