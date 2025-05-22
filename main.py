import time
from telegram_mejorado_pi import enviar_alerta_telegram
from detector_valuebets import analizar_valuebets
from detector_trampas import analizar_trampas
from detector_bonos import analizar_bonos

TOKEN_TELEGRAM = "7566801240:AAF-VrtRg4sexDFZ24azNz9AdpQc626xTnE"
CHAT_ID = "1454815028"

def modo_dany_hibrida():
    while True:
        print("Escaneando jugadas ocultas...")
        valor = analizar_valuebets()
        if valor:
            enviar_alerta_telegram(valor, "https://www.rushbet.co", TOKEN_TELEGRAM, CHAT_ID)

        print("Escaneando trampas de mercado...")
        trampa = analizar_trampas()
        if trampa:
            enviar_alerta_telegram(trampa, "https://www.rushbet.co", TOKEN_TELEGRAM, CHAT_ID)

        print("Buscando bonos activos...")
        bono = analizar_bonos()
        if bono:
            enviar_alerta_telegram(bono, "https://www.rushbet.co/promociones", TOKEN_TELEGRAM, CHAT_ID)

        time.sleep(30)

if __name__ == "__main__":
    print("DanyDarkBot V2 activa. Modo cazadora híbrida ON.")
    modo_dany_hibrida()
