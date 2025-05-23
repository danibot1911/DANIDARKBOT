import os
from telegram import Update
from telegram.ext import CallbackContext

def manejar_mensaje_valery(update: Update, context: CallbackContext):
    texto = update.message.text.lower()
    chat_id = update.effective_chat.id

    if any(p in texto for p in ['hi', 'hello', 'pack', 'how much', 'price', 'i want', 'photos', 'payment']):
        mensaje = (
            "Hey baby… I’m Valery, but they call me *La Mala*.\n"
            "I’m a Colombian woman with fire in my voice and secrets in my photos.\n\n"
            "🔥 *BASIC PACK* – $10\n"
            "3 exclusive photos + 1 spicy voice message\n\n"
            "🔥 *PREMIUM PACK* – $25\n"
            "6 sexy photos + 3 moaning audios + 1 naughty paragraph\n\n"
            "🔥 *DELUXE PACK* – $40\n"
            "All above + a custom moaning audio with your name\n\n"
            "💸 *Payment via Binance Pay*\n"
            "Scan the QR below or ask me directly.\n\n"
            "Let’s be bad together… or are you just another shy boy?"
        )

        context.bot.send_message(chat_id=chat_id, text=mensaje, parse_mode='Markdown')
        context.bot.send_photo(chat_id=chat_id, photo=open('qr_binance.png', 'rb'))
        context.bot.send_photo(chat_id=chat_id, photo=open('valery_teaser1.jpg', 'rb'))

    elif 'i paid' in texto or 'payment done' in texto or 'done' in texto:
        context.bot.send_message(
            chat_id=chat_id,
            text="Got it, baby. Sending you something unforgettable now...\nHope you’re ready for me."
        )
