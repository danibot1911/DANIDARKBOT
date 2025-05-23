import os
from flask import Flask, request
import telegram

# Configuración
TOKEN = "7566801240:AAFGVOjPdIMG2eUIyXRiua4YCmUDBWaxEAc"
bot = telegram.Bot(token=TOKEN)

# Flask app
app = Flask(__name__)

@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    chat_id = update.effective_chat.id
    message = update.message.text.lower()

    # 1. Saludo inicial
    if any(word in message for word in ['hi', 'hello', 'start', 'hey', 'hola']):
        welcome = (
            "Hey baby… I'm *Valery*, but they call me *La Mala*.\n\n"
            "🔥 *BASIC PACK* – $12\n"
            "6 spicy photos + 1 naughty voice note\n\n"
            "🔥 *PREMIUM PACK* – $28\n"
            "10 sexy pics + 2 moans + 1 short hot video\n\n"
            "🔥 *DELUXE PACK* – $45\n"
            "All above + custom voice note with your name\n\n"
            "❤️ Scan the QR below to pay with *Binance Pay*.\n"
            "Once paid, send me: 'I paid'\n\n"
            "*Let’s get nasty, papi...*"
        )
        bot.send_message(chat_id=chat_id, text=welcome, parse_mode='Markdown')
        bot.send_photo(chat_id=chat_id, photo=open("valery_teaser1.jpg", "rb"))
        bot.send_photo(chat_id=chat_id, photo=open("qr_binance.png", "rb"))

    # 2. Confirmación de pago
    elif "i paid" in message or "ya pagué" in message:
        bot.send_message(chat_id=chat_id, text="I got your payment, baby. Sending your private pack now…")

        # Elegir qué pack enviar (por ahora enviaremos basic por defecto)
        pack_folder = "packs/basic"
        for file in os.listdir(pack_folder):
            file_path = os.path.join(pack_folder, file)
            if file.lower().endswith((".jpg", ".jpeg", ".png", ".mp4")):
                bot.send_document(chat_id=chat_id, document=open(file_path, "rb"))

    else:
        bot.send_message(chat_id=chat_id, text="Talk to me, babe. I'm right here…")

    return "ok"

@app.route('/')
def index():
    return "Valery La Mala is live."

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
