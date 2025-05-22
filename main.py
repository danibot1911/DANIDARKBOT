# main.py

import asyncio
from connectors.telegram_mejorado_pi import TelegramConnectorMejorado
from modo_sniper_asistido import ejecutar_modo_sniper_asistido
from modo_ruleta_sombra import ejecutar_modo_ruleta_sombra
from rushbet_acceso_automatizado import iniciar_sesion_rushbet
import os

# Configuración directa (puedes reemplazar por os.getenv si usas .env)
TELEGRAM_TOKEN = '7566801240:AAF-VrtRg4sexDFZ24azNz9AdpQc626xTnE'
TELEGRAM_CHAT_ID = '1454815028'

async def main():
    print("Iniciando DaniDarkBot...")
    
    # Inicia conexión Telegram
    telegram = TelegramConnectorMejorado(token=TELEGRAM_TOKEN, chat_id=TELEGRAM_CHAT_ID)
    
    # Envia mensaje inicial
    await telegram.send_message("DaniDarkBot está despierta y cazando patrones en la ruleta.")

    # Iniciar sesión automatizada en RushBet
    iniciar_sesion_rushbet(usuario='andresgot11@gmail.com', contrasena='Emidaso19$')

    # Ejecutar ambos modos en paralelo
    await asyncio.gather(
        ejecutar_modo_ruleta_sombra(telegram),
        ejecutar_modo_sniper_asistido(telegram)
    )

if __name__ == '__main__':
    asyncio.run(main())

