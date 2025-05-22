import asyncio
from utils.telegram_mejorado_pi import iniciar_bot
from utils.rushbet_acceso_automatizado import analizar_rushbet
from utils.modo_sniper_asistido import modo_sniper_asistido

async def ejecutar_bot():
    print(">>> [DaniDarkBot] Activada en modo sombra.")
    await iniciar_bot()

def iniciar_rutinas():
    print(">>> [DaniDarkBot] Ejecutando vigilancia automática en RushBet...")
    analizar_rushbet()  # Escaneo automático de ruleta RushBet
    modo_sniper_asistido()  # Activación de sniper si estás online

if __name__ == "__main__":
    try:
        asyncio.run(ejecutar_bot())  # Conexión Telegram
        iniciar_rutinas()            # Rutinas automatizadas
    except Exception as e:
        print(f"[ERROR FATAL] {e}")

