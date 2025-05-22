import random

def analizar_bonos():
    posibles_bonos = [
        {"nombre": "Freebet sorpresa", "activo": True},
        {"nombre": "Cashback martes", "activo": False},
        {"nombre": "Bono ruleta diaria", "activo": True},
    ]

    bono = random.choice(posibles_bonos)

    if bono["activo"]:
        return f"🎁 BONO DETECTADO 🎁\n\n{bono['nombre']} está activo en tu cuenta. Entra ya a reclamarlo."

    return None
