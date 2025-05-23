from flask import Flask, request
import telegram
import os

TOKEN = "7566801240:AAFGVOjPdIMG2eUIyXRiua4YCmUDBWaxEAc"  # ← tu token real
bot = telegram.Bot(token=TOKEN)

app = Flask(__name__)

@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    chat_id = update.effective_chat.id
    message = update.message.text

    # Respuesta básica del bot
    bot.send_message(chat_id=chat_id, text=f"Hola mi amor, recibí: '{message}'")
    return 'ok'

@app.route('/')
def index():
    return 'DaniDarkBot está activo.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
