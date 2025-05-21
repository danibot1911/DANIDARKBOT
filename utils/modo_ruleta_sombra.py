import time
from utils.analizador_ruleta import analizar_secuencia
from utils.telegram_connector_mejorado import enviar_mensaje_telegram

from utils.rushbet_scraper import obtener_numeros_ruleta  # (si tienes esta lógica)

secuencia = obtener_numeros_ruleta()

def modo_ruleta_sombra():
    while True:
        for secuencia in secuencias_simuladas:
            resultado = analizar_secuencia(secuencia)
            mensaje = resultado.get("mensaje")
            if mensaje:
                enviar_mensaje_telegram(str(resultado))
        time.sleep(20)  # Tiempo entre análisis (puedes ajustar)

from utils.telegram_connector_mejorado import enviar_mensaje_telegram

if patrones_detectados:
    mensaje = {
        "mensaje": f"Se detectaron {len(patrones_detectados)} patrones consecutivos",
        "secuencia": secuencia,
        "patrones_detectados": patrones_detectados
    }
    enviar_mensaje_telegram(mensaje)

if len(patrones_detectados) >= 3:
    enviar_mensaje_telegram(mensaje)

if __name__ == "__main__":
    while True:
        try:
            ejecutar_modo_sombra()
            time.sleep(60)  # espera entre cada escaneo
        except Exception as e:
            print(f"[ERROR MODO SOMBRA] {e}")
