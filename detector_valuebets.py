import random

def analizar_valuebets():
    partidos = [
        {"equipo": "Real Madrid", "favorito": True, "posecion": 68, "tiros": 11, "va_perdiendo": True},
        {"equipo": "River Plate", "favorito": False, "posecion": 52, "tiros": 7, "va_perdiendo": False},
        {"equipo": "Man City", "favorito": True, "posecion": 75, "tiros": 14, "va_perdiendo": True},
    ]

    seleccionado = random.choice(partidos)

    if seleccionado["favorito"] and seleccionado["va_perdiendo"] and seleccionado["posecion"] > 60 and seleccionado["tiros"] >= 10:
        return f"🎯 JUGADA OCULTA DETECTADA 🎯\n\n{seleccionado['equipo']} domina el partido pero va perdiendo.\n⚠️ Apuesta estratégica al EMPATE o GOL pronto."

    return None
