import time
import asyncio
from utils.frontutils_telegram_mejorado import enviar_mensaje_telegram
from utils.ruleta_acceso_automatizado import iniciar_sesion_rushbet, buscar_patrones_ruleta
from utils.modo_asistido import verificar_estado_usuario

TOKEN = "7566801240:AAF-VrtRg4sexDFZ24azNz9AdpQc626xTnE"
CHAT_ID = "1454815028"

async def iniciar_bot():
    print("Iniciando sesión en RushBet...")
    sesion = iniciar_sesion_rushbet("andresgot11@gmail.com", "Emidaso19$")
    
    if not sesion:
        await enviar_mensaje_telegram(TOKEN, CHAT_ID, "No se pudo iniciar sesión en RushBet.")
        return

    await enviar_mensaje_telegram(TOKEN, CHAT_ID, "Sesión iniciada. Escaneando ruleta...")
    
    while True:
        conectado = verificar_estado_usuario()
        
        patrones = buscar_patrones_ruleta(sesion)
        
        if patrones:
            mensaje = f"Oportunidad detectada en ruleta: {patrones}"
            await enviar_mensaje_telegram(TOKEN, CHAT_ID, mensaje)
        else:
            if conectado:
                await enviar_mensaje_telegram(TOKEN, CHAT_ID, "Estoy online, pero sin oportunidades fuertes aún.")
        
        await asyncio.sleep(30)  # Escaneo cada 30 segundos

if __name__ == "__main__":
    asyncio.run(iniciar_bot())

