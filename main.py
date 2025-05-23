import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from valery_bot import manejar_mensaje_valery
from dotenv import load_dotenv
from flask import Flask, request

load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

app_telegram = Application.builder().token(TOKEN).build()

# Ruta Flask
flask_app = Flask(__name__)

@flask_app.route("/")
def index():
    return "Bot is alive!"

@flask_app.route(f"/webhook/{TOKEN}", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), app_telegram.bot)
    app_telegram.update_queue.put(update)
    return "ok"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hola, soy Valery.")

app_telegram.add_handler(CommandHandler("start", start))
app_telegram.add_handler(MessageHandler(filters.TEXT, manejar_mensaje_valery))

async def set_webhook():
    await app_telegram.bot.set_webhook(f"{WEBHOOK_URL}/webhook/{TOKEN}")

app_telegram.run_polling = lambda: None  # Evita que se ejecute polling por error
app_telegram.initialize()
app_telegram.post_init = set_webhook
