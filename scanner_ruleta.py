import random

def obtener_tiradas_simuladas():
    return [random.randint(0, 36) for _ in range(10)]

def es_rojo(numero):
    rojos = {1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36}
    return numero in rojos

def detectar_patron_ruleta():
    tiradas = obtener_tiradas_simuladas()
    print(f"Tiradas simuladas: {tiradas}")

    ultimos_3 = tiradas[-3:]

    # 1. Tres pares seguidos
    if all(n % 2 == 0 for n in ultimos_3):
        return {
            "tipo": "Tres pares seguidos",
            "explicacion": f"Números: {ultimos_3}"
        }

    # 2. Tres impares seguidos
    if all(n % 2 == 1 for n in ultimos_3 if n != 0):
        return {
            "tipo": "Tres impares seguidos",
            "explicacion": f"Números: {ultimos_3}"
        }

    # 3. Tres rojos seguidos
    if all(es_rojo(n) for n in ultimos_3 if n != 0):
        return {
            "tipo": "Tres rojos seguidos",
            "explicacion": f"Números: {ultimos_3}"
        }

    # 4. Tres negros seguidos
    if all(not es_rojo(n) and n != 0 for n in ultimos_3):
        return {
            "tipo": "Tres negros seguidos",
            "explicacion": f"Números: {ultimos_3}"
        }

    # 5. Tres altos seguidos (>18)
    if all(n > 18 for n in ultimos_3):
        return {
            "tipo": "Tres números altos seguidos",
            "explicacion": f"Números: {ultimos_3}"
        }

    # 6. Tres bajos seguidos (1-18)
    if all(0 < n <= 18 for n in ultimos_3):
        return {
            "tipo": "Tres números bajos seguidos",
            "explicacion": f"Números: {ultimos_3}"
        }

    # 7. Zeros múltiples
    if tiradas.count(0) >= 2:
        return {
            "tipo": "Reaparición de ceros",
            "explicacion": f"El 0 apareció varias veces: {tiradas}"
        }

    # 8. Cero ausente en 10 tiradas
    if 0 not in tiradas:
        return {
            "tipo": "Ausencia prolongada de 0",
            "explicacion": "El número 0 no ha salido en las últimas 10 tiradas"
        }

    return None
