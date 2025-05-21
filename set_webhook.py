import telegram

TOKEN = '7566801240:AAHMnnCTacnesKOPrUwMcuHRArUB3IoZ1bk'
WEBHOOK_URL = 'https://s3t-ruleta.onrender.com/webhook'

bot = telegram.Bot(token=TOKEN)
set_hook = bot.set_webhook(WEBHOOK_URL)

if set_hook:
    print("Webhook activado correctamente.")
else:
    print("Error al activar webhook.")
