from utils.templates.boton_generator import generar_boton_apuesta
from utils.analizador_ruleta import analizar_patron_ruleta

def detectar_sniper_asistido(mensaje, secuencia):
    try:
        if not secuencia or len(secuencia) < 7:
            return {"respuesta": "Sin datos de secuencia."}

        resultado = analizar_patron_ruleta(secuencia)

        if resultado:
            texto = (
                f"**ALERTA S3T RULETA – MODO ORO ACTIVADO**\n\n"
                f"{resultado}\n"
                f"Recomendación: Apostar NEGRO."
            )
            boton = generar_boton_apuesta("Abrir Ruleta", "https://rushbet.co")
            return {"respuesta": texto, "boton": boton}

        return {"respuesta": "No se detectó ningún patrón válido."}

    except Exception as e:
        return {"error": str(e)}
