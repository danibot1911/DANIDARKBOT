import telegram
import traceback

class TelegramConnectorMejorado:
    def __init__(self, bot, chat_id):
        self.bot = bot
        self.chat_id = chat_id

    def procesar_mensaje(self, data):
        try:
            mensaje = self.extraer_mensaje(data)
            if mensaje:
                texto = mensaje.get("text", "")
                if texto:
                    print(f"[MENSAJE RECIBIDO]: {texto}")
                    self.bot.send_message(chat_id=self.chat_id, text=f"Recibido: {texto}")
                else:
                    print("[AVISO] Mensaje sin texto.")
            else:
                print("[AVISO] No se pudo extraer mensaje.")
        except Exception as e:
            print(f"[ERROR] procesando mensaje: {e}")
            traceback.print_exc()

    def extraer_mensaje(self, data):
        try:
            if "message" in data:
                return data["message"]
            elif "edited_message" in data:
                return data["edited_message"]
            elif "callback_query" in data and "message" in data["callback_query"]:
                return data["callback_query"]["message"]
        except Exception as e:
            print(f"[ERROR] extrayendo mensaje: {e}")
        return None
