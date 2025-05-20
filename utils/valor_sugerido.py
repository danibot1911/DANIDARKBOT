# utils/valor_sugerido.py

def calcular_valor_apuesta(confianza):
    if confianza >= 9:
        return 100000
    elif confianza >= 7:
        return 50000
    elif confianza >= 5:
        return 30000
    elif confianza >= 3:
        return 20000
    else:
        return 10000# valor por defecto
