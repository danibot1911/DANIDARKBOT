import time
from utils.analizador_ruleta import analizar_secuencia
from utils.telegram_connector_mejorado import enviar_mensaje_telegram
from utils.rushbet_scraper import obtener_numeros_ruleta  # usa datos reales de RushBet

def modo_ruleta_sombra():
    while True:
        try:
            secuencia = obtener_numeros_ruleta()  # números en vivo
            if not secuencia or len(secuencia) < 5:
                time.sleep(10)
                continue

            resultado = analizar_secuencia(secuencia)
            mensaje = resultado.get("mensaje")
            patrones_detectados = resultado.get("patrones_detectados", [])

            if patrones_detectados:
                mensaje_alerta = (
                    f"DanyDarkBot activada\n"
                    f"Hora: {time.strftime('%H:%M:%S')}\n\n"
                    f"Patrón detectado en ruleta\n"
                    f"Probabilidad de acierto: ALTA\n\n"
                    f"Actúa rápido, amor"
                )
                enviar_mensaje_telegram(mensaje_alerta)

            time.sleep(30)  # espera entre ciclos

        except Exception as e:
            print(f"[ERROR MODO SOMBRA] {e}")
            time.sleep(60)
