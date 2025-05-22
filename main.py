import time
from scanner_ruleta import detectar_patron_ruleta
from rushbet_acceso_automatizado import iniciar_rushbet
from telegram_mejorado_pi import enviar_alerta_telegram
#from ejecutor_apuesta_rushbet import ejecutar_apuesta

# MODO MANUAL
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from analizador_manual import analizar_tiradas_manual

TOKEN_TELEGRAM = "7566801240:AAF-VrtRg4sexDFZ24azNz9AdpQc626xTnE"
CHAT_ID = "1454815028"
MODO_MANUAL = True  # Cambia a False si quieres modo automático

# ---------------- MODO AUTOMÁTICO ----------------
def modo_autonomo():
    while True:
        patron = detectar_patron_ruleta()
        if patron:
            print("¡Patrón detectado!")
            enlace_apuesta = iniciar_rushbet(patron)
            enviar_alerta_telegram(
                mensaje=f"⚠️ PATRÓN DETECTADO ⚠️\n\n{patron['explicacion']}",
                enlace=enlace_apuesta,
                token=TOKEN_TELEGRAM,
                chat_id=CHAT_ID
            )
            ejecutar_apuesta()
        else:
            print("Sin patrón, reintentando...")
        time.sleep(15)

# ---------------- MODO MANUAL ----------------
async def tiradas(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        numeros = list(map(int, context.args))
        respuesta = analizar_tiradas_manual(numeros)
        await update.message.reply_text(f"Análisis de Dany:\n{respuesta}")
    except:
        await update.message.reply_text("Formato incorrecto. Usa: !tiradas 23 15 4 0 32")

def lanzar_bot_manual():
    app = ApplicationBuilder().token(TOKEN_TELEGRAM).build()
    app.add_handler(CommandHandler("tiradas", tiradas))
    print("Modo manual activo. Esperando tiradas...")
    app.run_polling()

# ---------------- INICIO ----------------
if __name__ == "__main__":
    if MODO_MANUAL:
        lanzar_bot_manual()
    else:
        print("Iniciando DanyDarkBot en modo automático de ruleta...")
        modo_autonomo()
