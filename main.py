import asyncio
from utils.telegram_mejorado_pi import TelegramConnectorMejorado
from utils.rushbet_acceso_automatizado import analizar_rushbet
from utils.modo_sniper_asistido import ejecutar_modo_asistido
from utils.modo_ruleta_sombra import ejecutar_modo_sombra

# Inicializamos la clase de Telegram
telegram_bot = TelegramConnectorMejorado()

async def iniciar_bot():
    try:
        # Paso 1: Confirmar conexión con Telegram
        telegram_bot.send_alert("DaniDarkBot activada, mami. Estoy en modo sniper...")

        # Paso 2: Iniciar análisis de RushBet automatizado (modo directo)
        analizar_rushbet()

        # Paso 3: Ejecutar en paralelo los dos modos activos
        await asyncio.gather(
            ejecutar_modo_asistido(telegram_bot),
            ejecutar_modo_sombra(telegram_bot)
        )

    except Exception as e:
        print(f"[ERROR GRAVE] Falla al iniciar bot: {e}")
        telegram_bot.send_alert(f"[ERROR] DaniDarkBot tuvo una falla: {e}")

if __name__ == "__main__":
    asyncio.run(iniciar_bot())

