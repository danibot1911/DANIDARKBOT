from utils.analizador_ruleta import analizar_patron_ruleta
from templates.boton_generator import generar_boton_apuesta

def detectar_sniper_asistido(datos):
    mensaje = datos.get("mensaje", "ALERTA")
    secuencia = datos.get("secuencia", [])

    if not secuencia or len(secuencia) < 7:
        return {"respuesta": "Sin datos de secuencia."}

    resultado = analizar_patron_ruleta(secuencia)

    if resultado:
        boton = generar_boton_apuesta("Ir a RushBet", "https://www.rushbet.co")
        return {
            "respuesta": f"{mensaje.upper()}\n\n{resultado}",
            "boton": boton
        }

    return {"respuesta": "No se detectaron patrones."}
