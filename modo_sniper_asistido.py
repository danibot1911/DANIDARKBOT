from utils.analizador_ruleta import analizar_patron_ruleta

def detectar_sniper_asistido(datos):
    secuencia = datos.get("secuencia", [])
    if not secuencia:
        return {"respuesta": "Sin datos de secuencia."}

    mensaje = analizar_patron_ruleta(secuencia)
    if mensaje:
        return {"respuesta": mensaje}
    else:
        return {"respuesta": "Sin patrón detectado"}
