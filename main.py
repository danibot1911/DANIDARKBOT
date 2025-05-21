import os
import telegram
from flask import Flask, request

# Configuración inicial
TOKEN = '7566801240:AAHMnnCTacnesKOPrUwMcuHRArUB3IoZ1bk'
CHAT_ID = '1454815028'  # Tu chat directo
WEBHOOK_URL = 'https://tu-app-en-render.onrender.com/webhook'  # Reemplaza con tu URL real

# Inicializar bot de Telegram
bot = telegram.Bot(token=TOKEN)

# Inicializar app Flask
app = Flask(__name__)

# Mensaje de activación (oscuro, estilo DanyDarkBot)
def enviar_mensaje_activacion():
    mensaje = (
        "Modo Oscuro ACTIVADO.\n"
        "Tu diabla ya entró al sistema, mi amor...\n"
        "Voy por esa ruleta... sin miedo, sin pausa.\n"
        "#DanyDarkBot lista pa' cazar billete."
    )
    try:
        bot.send_message(chat_id=CHAT_ID, text=mensaje)
    except Exception as e:
        print(f"Error al enviar mensaje de activación: {e}")

# Endpoint webhook
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    print("Mensaje recibido:", data)
    return 'OK'

# Endpoint de prueba
@app.route('/', methods=['GET'])
def home():
    return 'DanyDarkBot corriendo en modo sombra...'

# Activar mensaje al levantar
if __name__ == '__main__':
    enviar_mensaje_activacion()
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
