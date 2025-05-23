import os
from flask import Flask, request
from telegram import Update, Bot
from telegram.ext import Application, CallbackContext, CommandHandler
from telegram.ext import Dispatcher

TOKEN = os.getenv("TELEGRAM_TOKEN")
bot = Bot(token=TOKEN)

# Flask app
app = Flask(__name__)

# Telegram app
telegram_app = Application.builder().token(TOKEN).build()
dispatcher: Dispatcher = telegram_app.dispatcher

# Comando básico
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Hola! Soy Valery, ya estoy activa.")

# Registrar comandos
dispatcher.add_handler(CommandHandler("start", start))

# Ruta Webhook
@app.route(f'/{TOKEN}', methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return "ok"

# Ruta de prueba
@app.route("/", methods=["GET"])
def home():
    return "Bot activo y escuchando..."

if __name__ == "__main__":
    PORT = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=PORT)
