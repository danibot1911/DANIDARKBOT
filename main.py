import os
import time
import telebot
from binance.client import Client
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

client = Client(API_KEY, API_SECRET)
bot = telebot.TeleBot(TELEGRAM_TOKEN)

def enviar_alerta(texto):
    try:
        bot.send_message(CHAT_ID, f"🔥 DaniSniperX:\n\n{texto}")
    except Exception as e:
        print("Error enviando mensaje:", e)

def analizar_futuros():
    try:
        tickers = client.futures_ticker()
        for coin in tickers:
            symbol = coin['symbol']
            priceChangePercent = float(coin['priceChangePercent'])

            if abs(priceChangePercent) > 5 and symbol.endswith("USDT"):
                mensaje = f"Movimiento fuerte en {symbol}\nCambio: {priceChangePercent}%"
                enviar_alerta(mensaje)
    except Exception as e:
        print("Error analizando futuros:", e)

if __name__ == "__main__":
    while True:
        analizar_futuros()
        time.sleep(60)
