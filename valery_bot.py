import os
from telegram import Update
from telegram.ext import CallbackContext

async def manejar_mensaje_valery(update: Update, context: CallbackContext):
    texto = update.message.text.lower()
    chat_id = update.effective_chat.id

    if any(p in texto for p in ['hi', 'hello', 'hola', 'valery']):
        mensaje = (
            "Hey baby… I’m Valery, but they call me *La Mala*.\n"
            "I’m a Colombian woman with fire in her veins.\n\n"
            "🔥 *BASIC PACK* – $10\n"
            "3 exclusive photos + 1 spicy voice note.\n\n"
            "🔥 *PREMIUM PACK* – $25\n"
            "6 sexy photos + 3 moaning audios + short tease.\n\n"
            "🔥 *DELUXE PACK* – $40\n"
            "All above + a custom moaning audio just for you.\n\n"
            "🪙 *Payment via Binance Pay*\n"
            "Scan the QR below or ask me directly.\n"
            "Let’s be bad together… or are you scared?"
        )

        await context.bot.send_message(chat_id=chat_id, text=mensaje, parse_mode="Markdown")
        await context.bot.send_photo(chat_id=chat_id, photo=open('qr_binance.png', 'rb'))
        await context.bot.send_photo(chat_id=chat_id, photo=open('valery_teaser1.jpg', 'rb'))

    elif 'i paid' in texto or 'payment done' in texto or 'listo' in texto:
        await context.bot.send_message(
            chat_id=chat_id,
            text="Got it, baby. Sending you something hot right now…"
        )
