import os
from telegram.ext import Application, MessageHandler, filters
from valery_bot import manejar_mensaje_valery
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")

from valery_bot import manejar_mensaje_valery

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT, manejar_mensaje_valery))
    app.run_polling()

if __name__ == "__main__":
    main()
