from utils.templates.boton_generator import generar_boton_apuesta
from utils.analizador_ruleta import analizar_patron_ruleta
from utils.valor_sugerido import calcular_valor_apuesta
from utils.telegram_connector_mejorado import enviar_mensaje

enviar_alerta_ruleta(mensaje, valor)
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

            mensaje = "Patrón de 7 rojos detectado. Hora de meterle al negro con confianza nivel 4."
            nivel_confianza = 4
            valor = calcular_valor_apuesta(nivel_confianza)
           
            boton = generar_boton_apuesta("Abrir Ruleta", "https://rushbet.co")
            return {"respuesta": texto, "boton": boton}

        return {"respuesta": "No se detectó ningún patrón válido."}

    except Exception as e:
        return {"error": str(e)}
