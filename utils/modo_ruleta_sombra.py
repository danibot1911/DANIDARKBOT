import time
from utils.analizador_ruleta import analizar_secuencia
from utils.telegram_connector_mejorado import enviar_mensaje_telegram

# Simulación: puedes reemplazar esto por conexión a una API o archivo real
secuencias_simuladas = [
    [17, 3, 5, 7, 9],
    [2, 4, 6, 8, 10],
    [25, 12, 12, 12, 12],
    [1, 2, 3, 5, 8],
    [33, 0, 33, 0, 33],
]

def modo_ruleta_sombra():
    while True:
        for secuencia in secuencias_simuladas:
            resultado = analizar_secuencia(secuencia)
            mensaje = resultado.get("mensaje")
            if mensaje:
                enviar_mensaje_telegram(str(resultado))
        time.sleep(20)  # Tiempo entre análisis (puedes ajustar)

from utils.telegram_connector_mejorado import enviar_mensaje_telegram

mensaje = {
    "mensaje": "Alerta de prueba desde el modo sombra",
    "secuencia": [1, 3, 5, 7, 9],
    "patrones_detectados": [[1, 3], [3, 5], [5, 7]]
}
enviar_mensaje_telegram(str(mensaje))
time.sleep(30)  # Espera antes de seguir el loop


if __name__ == "__main__":
    modo_ruleta_sombra()
