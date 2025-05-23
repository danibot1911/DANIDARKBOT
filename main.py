import os
from flask import Flask, request
from telegram import Update
from telegram.ext import Application, CallbackContext, MessageHandler, filters
from valery_bot import manejar_mensaje_valery
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")
BOT_URL = os.getenv("BOT_URL")  # Asegúrate de configurar esta variable en Render

app = Flask(__name__)
application = Application.builder().token(TOKEN).build()

# Añadir manejador
application.add_handler(MessageHandler(filters.TEXT, manejar_mensaje_valery))

@app.route("/")
def home():
    return "ValeryBot online - Render Webhook Mode"

@app.route(f"/{TOKEN}", methods=["POST"])
def receive_update():
    update = Update.de_json(request.get_json(force=True), application.bot)
    application.update_queue.put(update)
    return "ok", 200

if __name__ == "__main__":
    application.run_webhook(
        listen="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        url_path=TOKEN,
        webhook_url=f"{BOT_URL}/{TOKEN}"
    )
