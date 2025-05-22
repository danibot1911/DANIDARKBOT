import os
import telegram

TOKEN = "7566801240:AAF-VrtRg4sexDFZ24azNz9AdpQc626xTnE"
CHAT_ID = "1454815028"

bot = telegram.Bot(token=TOKEN)

def enviar_mensaje_telegram(mensaje):
    try:
        bot.send_message(chat_id=CHAT_ID, text=mensaje, parse_mode="HTML")
        print("Mensaje enviado a Telegram.")
    except Exception as e:
        print(f"[ERROR] al enviar mensaje: {e}")
