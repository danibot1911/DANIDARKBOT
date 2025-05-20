from utils.analizador_ruleta import analizar_patron_ruleta

def detectar_sniper_asistido(mensaje, secuencia=None):
    if not secuencia:
        return {"respuesta": "Sin datos de secuencia."}

    analisis = analizar_patron_ruleta(secuencia)
    if analisis:
        return {"respuesta": f"Alerta Sniper: {analisis}"}
    else:
        return {"respuesta": "Sin coincidencias."}
