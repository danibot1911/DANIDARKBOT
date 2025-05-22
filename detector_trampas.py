import random

def analizar_trampas():
    movimientos = [
        {"partido": "Nacional vs Santa Fe", "cuota_inicial": 2.80, "cuota_actual": 1.95},
        {"partido": "Tolima vs América", "cuota_inicial": 1.60, "cuota_actual": 1.55},
        {"partido": "Junior vs Cali", "cuota_inicial": 3.10, "cuota_actual": 2.10},
    ]

    elegido = random.choice(movimientos)
    variacion = abs(elegido["cuota_inicial"] - elegido["cuota_actual"])

    if variacion >= 0.8:
        return f"⚠️ POSIBLE TRAMPA ⚠️\n\n{elegido['partido']}\nLa cuota bajó de {elegido['cuota_inicial']} a {elegido['cuota_actual']} de forma brusca.\nRevisa antes de apostar."

    return None
