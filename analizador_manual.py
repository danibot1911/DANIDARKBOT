def analizar_tiradas_manual(tiradas):
    if len(tiradas) < 3:
        return "Se necesitan al menos 3 números para analizar."

    ultimos_3 = tiradas[-3:]

    if all(n % 2 == 0 for n in ultimos_3):
        return f"Patrón detectado: Tres pares seguidos ({ultimos_3})"

    if all(n % 2 == 1 for n in ultimos_3 if n != 0):
        return f"Patrón detectado: Tres impares seguidos ({ultimos_3})"

    rojos = {1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36}

    if all(n in rojos for n in ultimos_3 if n != 0):
        return f"Patrón detectado: Tres rojos seguidos ({ultimos_3})"

    if all(n not in rojos and n != 0 for n in ultimos_3):
        return f"Patrón detectado: Tres negros seguidos ({ultimos_3})"

    if tiradas.count(0) >= 2:
        return "¡Ojo! El 0 apareció más de una vez."

    if 0 not in tiradas:
        return "Cero ausente en las últimas tiradas (puede ser jugada estratégica)."

    return "No se detectó ningún patrón fuerte en esas tiradas."
