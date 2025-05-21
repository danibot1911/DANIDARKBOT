def analizar_secuencia(secuencia):
    if not secuencia or not isinstance(secuencia, list):
        return {
            "mensaje": "Secuencia inválida.",
            "secuencia": []
        }

    # Detección básica de patrones consecutivos
    patrones = []
    for i in range(len(secuencia) - 1):
        if secuencia[i + 1] - secuencia[i] == 2:
            patrones.append((secuencia[i], secuencia[i + 1]))

    mensaje = f"Se detectaron {len(patrones)} posibles patrones consecutivos de +2." if patrones else "No se detectaron patrones."
    
    return {
        "mensaje": mensaje,
        "secuencia": secuencia,
        "patrones_detectados": patrones
    }
