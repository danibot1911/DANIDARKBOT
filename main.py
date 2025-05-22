import asyncio
from connectors.telegram_mejorado_pi import TelegramConnectorMejorado
from rushbet_acceso_automatizado import iniciar_acceso_rushbet, detectar_patrones_ruleta
import logging

# Configuración de logging
logging.basicConfig(level=logging.INFO)

# Parámetros fijos (sin .env)
BOT_TOKEN = '7566801240:AAF-VrtRg4sexDFZ24azNz9AdpQc626xTnE'
CHAT_ID = 1454815028
LINK_RULETA = "https://www.rushbet.co/?page=all-games&game=225"

# Modo actual
MODO_AUTONOMO = True
MODO_ASISTIDO = True  # Se activa si tú estás en línea

# Inicializar conexión con Telegram
telegram_bot = TelegramConnectorMejorado(BOT_TOKEN, CHAT_ID)

async def main():
    try:
        # Confirmar conexión al bot
        await telegram_bot.enviar_mensaje("DanyDarkBot encendida, modo autónomo activado.")
        
        # Acceder automáticamente a RushBet
        await iniciar_acceso_rushbet(usuario="andresgot11@gmail.com", contraseña="Emidaso19$")

        # Escanear patrones reales en ruleta
        while True:
            patrones = await detectar_patrones_ruleta()

            if patrones:
                for jugada in patrones:
                    mensaje = f"Oportunidad detectada en ruleta:\n\n{jugada}\n\n[Ingresar a RushBet]({LINK_RULETA})"
                    await telegram_bot.enviar_mensaje(mensaje, parse_mode='Markdown', link_preview=False)
            await asyncio.sleep(15)

    except Exception as e:
        logging.error(f"Error en ejecución principal: {e}")
        await telegram_bot.enviar_mensaje("Error detectado en DanyDarkBot. Revisión urgente.")
        raise

if __name__ == '__main__':
    asyncio.run(main())

