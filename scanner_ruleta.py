import random

# Simulación de historial de ruleta (sustituir con scraping real)
def obtener_tiradas_simuladas():
    return [random.randint(0, 36) for _ in range(10)]

def detectar_patron_ruleta():
    tiradas = obtener_tiradas_simuladas()
    print(f"Últimas tiradas: {tiradas}")

    if tiradas[-1] % 2 == 0 and tiradas[-2] % 2 == 0 and tiradas[-3] % 2 == 0:
        return {
            "tipo": "Patrón Par",
            "explicacion": f"Tres números pares seguidos: {tiradas[-3:]}"
        }

    if tiradas.count(0) >= 2:
        return {
            "tipo": "Cero recurrente",
            "explicacion": f"El 0 ha salido varias veces: {tiradas}"
        }

    return None
