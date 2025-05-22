import requests

def enviar_alerta_telegram(mensaje, enlace, token, chat_id):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": mensaje,
        "reply_markup": {
            "inline_keyboard": [[{"text": "Entrar a la Ruleta", "url": enlace}]]
        },
        "parse_mode": "HTML"
    }

    response = requests.post(url, json=payload)

    if response.status_code == 200:
        print("✅ Alerta enviada a Telegram.")
    else:
        print(f"❌ Error al enviar alerta: {response.text}")
