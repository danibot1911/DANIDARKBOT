import time
from utils.analizador_ruleta import analizar_secuencia
from utils.telegram_connector_mejorado import enviar_mensaje_telegram
from utils.rushbet_scraper import obtener_numeros_ruleta  # Asegúrate de tener este módulo

def modo_ruleta_sombra():
    while True:
        secuencias_simuladas = [obtener_numeros_ruleta()]  # Simulación simple (puedes expandir esto)
        for secuencia in secuencias_simuladas:
            resultado = analizar_secuencia(secuencia)
            patrones = resultado.get("patrones_detectados", [])

            if patrones:
                mensaje = {
                    "mensaje": f"Se detectaron {len(patrones)} posibles patrones consecutivos de +2.",
                    "secuencia": secuencia,
                    "patrones_detectados": patrones
                }
                enviar_mensaje_telegram(str(mensaje))

            time.sleep(20)  # Tiempo entre cada chequeo

if __name__ == "__main__":
    while True:
        try:
            modo_ruleta_sombra()
            time.sleep(60)
        except Exception as e:
            print(f"[ERROR MODO SOMBRA] {e}")
