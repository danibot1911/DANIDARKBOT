from flask import Flask, request
import telegram
import os
import json
from connectors.telegram_mejorado_pi import TelegramConnectorMejorado
from sistema_alertas_grupo import sistema_alertas_grupo
from config import TOKEN, CHAT_ID, WEBHOOK_URL

# Inicializa la aplicación Flask
app = Flask(__name__)

# Inicializa el bot de Telegram
bot = telegram.Bot(token=TOKEN)

# Instancia del conector mejorado
telegram_connector = TelegramConnectorMejorado(bot=bot, chat_id=CHAT_ID)

# Endpoint para Webhook de Telegram
@app.route(f"/{TOKEN}", methods=["POST"])
def webhook_handler():
    if request.method == "POST":
        try:
            data = json.loads(request.data.decode("utf-8"))
            telegram_connector.procesar_mensaje(data)
        except Exception as e:
            print(f"Error procesando mensaje: {e}")
        return "OK", 200

# Ruta raíz de prueba
@app.route("/", methods=["GET"])
def index():
    return "DANNYDARKBOT activo y cazando..."

# Lanzador de monitoreo (modo autónomo)
@app.route("/activar-alertas", methods=["GET"])
def activar_alertas():
    try:
        sistema_alertas_grupo()
        return "Sistema de alertas activado", 200
    except Exception as e:
        return f"Error activando alertas: {e}", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
