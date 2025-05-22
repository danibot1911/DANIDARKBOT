import time
from scanner_ruleta import detectar_patron_ruleta
from rushbet_acceso_automatizado import iniciar_rushbet
from telegram_mejorado_pi import enviar_alerta_telegram

TOKEN_TELEGRAM = "7566801240:AAF-VrtRg4sexDFZ24azNz9AdpQc626xTnE"
CHAT_ID = "1454815028"

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
        else:
            print("Sin patrón, reintentando...")
        time.sleep(15)

if __name__ == "__main__":
    print("Iniciando DanyDarkBot en modo autónomo de ruleta...")
    modo_autonomo()
