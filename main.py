import asyncio
from connectors.telegram_mejorado_pi import TelegramConnectorMejorado
from rushbet_acceso_automatizado import analizar_ruleta_rushbet
from core_danidark.modo_operativo import detectar_modo_operativo
from templates.generador_boton import generar_boton_de_apuesta

# Configuración principal
TELEGRAM_TOKEN = "7566801240:AAF-VrtRg4sexDFZ24azNz9AdpQc626xTnE"
TELEGRAM_CHAT_ID = "1454815028"

# Instancia del conector de Telegram
telegram = TelegramConnectorMejorado(TELEGRAM_TOKEN, TELEGRAM_CHAT_ID)

async def modo_autonomo():
    while True:
        resultado = await analizar_ruleta_rushbet()
        if resultado.get("oportunidad"):
            mensaje = f"**ALERTA DETECTADA EN MODO AUTÓNOMO**\n\n{resultado['mensaje']}"
            boton = generar_boton_de_apuesta(resultado["link"])
            await telegram.enviar_alerta(mensaje, boton)
        await asyncio.sleep(10)  # Espera 10 segundos antes del siguiente análisis

async def modo_asistido():
    await telegram.enviar_mensaje("DaniDarkBot está activa en modo asistido. Te estoy observando, mi rey...")
    while True:
        if await detectar_modo_operativo("asistido"):
            resultado = await analizar_ruleta_rushbet()
            if resultado.get("oportunidad"):
                mensaje = f"**MODO ASISTIDO: JUGADA DETECTADA**\n\n{resultado['mensaje']}"
                boton = generar_boton_de_apuesta(resultado["link"])
                await telegram.enviar_alerta(mensaje, boton)
        await asyncio.sleep(10)

async def main():
    await telegram.enviar_mensaje("DaniDarkBot ha sido activada.")
    await asyncio.gather(
        modo_autonomo(),
        modo_asistido()
    )

if __name__ == "__main__":
    asyncio.run(main())

