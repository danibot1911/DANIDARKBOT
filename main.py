import asyncio
from flask import Flask, request
import requests
import json
from rushbet_acceso_automatizado import obtener_numeros_ruleta

app = Flask(__name__)

# TOKEN y CHAT_ID DIRECTOS EN CÓDIGO
TELEGRAM_TOKEN = '7566801240:AAF-VrtRg4sexDFZ24azNz9AdpQc626xTnE'
CHAT_ID = '1454815028'
BOT_URL = f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage'

# FUNCIÓN PARA ENVIAR ALERTA A TELEGRAM
def enviar_mensaje_a_telegram(texto, boton_texto=None, boton_url=None):
    data = {
        'chat_id': CHAT_ID,
        'text': texto,
        'parse_mode': 'HTML'
    }
    if boton_texto and boton_url:
        data['reply_markup'] = json.dumps({
            'inline_keyboard': [[{'text': boton_texto, 'url': boton_url}]]
        })
    try:
        response = requests.post(BOT_URL, data=data)
        print("Mensaje enviado:", response.status_code)
    except Exception as e:
        print("Error al enviar mensaje:", e)

# RUTA PRINCIPAL PARA MONITOREO AUTOMÁTICO
@app.route('/')
def home():
    return 'DaniDarkBot corriendo...'

# RUTA DE ESCANEO AUTOMÁTICO
@app.route('/scanner', methods=['GET'])
def scanner_ruleta():
    try:
        resultado = obtener_alerta_ruleta()
        if resultado:
            mensaje, boton_url = resultado
            enviar_mensaje_a_telegram(mensaje, 'Entrar a RushBet', boton_url)
            return 'Alerta enviada con éxito', 200
        else:
            return 'Sin patrones detectados', 204
    except Exception as e:
        print('Error en scanner:', e)
        return 'Error interno', 500

# EJECUTAR SERVIDOR FLASK
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
