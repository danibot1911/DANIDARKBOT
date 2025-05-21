import telegram
import os

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

bot = telegram.Bot(token=TOKEN)


def enviar_mensaje_telegram(mensaje):
    try:
        bot.send_message(chat_id=CHAT_ID, text=mensaje, parse_mode=telegram.ParseMode.HTML)
        print("[DanyDarkBot] Mensaje enviado correctamente a Telegram.")
    except Exception as e:
        print(f"[DanyDarkBot] Error al enviar mensaje a Telegram: {e}")
