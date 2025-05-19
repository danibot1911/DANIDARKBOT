def analizar_patron_ruleta(secuencia):
    rojos = {1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36}
    negros = {2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35}

    ultimos = secuencia[-7:]
    conteo_rojos = sum(1 for n in ultimos if n in rojos)
    conteo_negros = sum(1 for n in ultimos if n in negros)

    if conteo_rojos >= 6:
        return f"Se detectaron {conteo_rojos} números ROJOS en las últimas 7 jugadas.\nRecomendación: **Apostar NEGRO**."
    if conteo_negros >= 6:
        return f"Se detectaron {conteo_negros} números NEGROS en las últimas 7 jugadas.\nRecomendación: **Apostar ROJO**."
    
    return None
