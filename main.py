import os
from telegram.ext import Application, MessageHandler, filters
from valery_bot import manejar_mensaje_valery
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, manejar_mensaje_valery))
    print("ValeryLaMala activa.")
    app.run_polling()

if __name__ == "__main__":
    main()
