from telegram import Update
from telegram.ext import CallbackContext

def manejar_mensaje_valery(update: Update, context: CallbackContext):
    texto = update.message.text.lower()
    chat_id = update.effective_chat.id

    if any(p in texto for p in ['hi', 'hello', 'hey', 'hola']):
        mensaje = (
            "Hey baby… I’m Valery, but they call me *La Mala*.\n"
            "I’m a Colombian woman with fire in her blood.\n\n"
            "🔥 *BASIC PACK* – $10\n3 exclusive photos + 1 spicy voice note\n\n"
            "🔥 *PREMIUM PACK* – $25\n6 sexy photos + 3 moaning audios + 1 short clip\n\n"
            "🔥 *DELUXE PACK* – $40\nAll above + a custom moaning audio\n\n"
            "🪙 *Payment via Binance Pay*\nScan the QR below or ask me directly.\n\n"
            "Let’s be bad together… or are you scared?"
        )

        context.bot.send_message(chat_id=chat_id, text=mensaje, parse_mode='Markdown')
        context.bot.send_photo(chat_id=chat_id, photo=open('valery_teaser1.jpg', 'rb'))
        context.bot.send_photo(chat_id=chat_id, photo=open('qr_binance.png', 'rb'))

    elif 'i paid' in texto or 'payment done' in texto:
        context.bot.send_message(chat_id=chat_id, text="Got it, baby. Sending you something hot now…")
