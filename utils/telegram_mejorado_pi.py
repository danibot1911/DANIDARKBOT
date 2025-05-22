import requests

class TelegramConnectorMejorado:
    def __init__(self, bot_token: str, chat_id: str):
        self.bot_token = bot_token
        self.chat_id = chat_id
        self.api_url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage"

    def enviar_mensaje(self, mensaje: str):
        payload = {
            "chat_id": self.chat_id,
            "text": mensaje,
            "parse_mode": "HTML"
        }
        try:
            response = requests.post(self.api_url, data=payload)
            if response.status_code != 200:
                print(f"[Telegram] Error al enviar mensaje: {response.text}")
            else:
                print("[Telegram] Mensaje enviado con éxito")
        except Exception as e:
            print(f"[Telegram] Excepción al enviar mensaje: {e}")

# Esta es la función que faltaba:
def iniciar_bot(bot_token: str, chat_id: str):
    bot = TelegramConnectorMejorado(bot_token, chat_id)
    bot.enviar_mensaje("DanyDarkBot activada correctamente.")
