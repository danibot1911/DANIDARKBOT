from flask import Flask, request
from connectors.telegram_mejorado_pi import TelegramConnectorMejorado
import os

# Inicializa Flask
app = Flask(__name__)

# Configura token y ID desde variables de entorno
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

# Instancia el conector
telegram_bot = TelegramConnectorMejorado(TELEGRAM_TOKEN, CHAT_ID)

# Ruta raíz (verificación simple)
@app.route('/')
def home():
    return 'DaniDarkBot está activa y lista para la ruleta.'

# Ruta que recibe las alertas POST desde otros módulos
@app.route('/alerta', methods=['POST'])
def recibir_alerta():
    try:
        data = request.json
        mensaje = data.get('mensaje', 'Sin mensaje')
        telegram_bot.send_alerta(mensaje)
        return {'status': 'ok'}, 200
    except Exception as e:
        return {'error': str(e)}, 500

# Arranque
if __name__ == '__main__':
    app.run(debug=True)
