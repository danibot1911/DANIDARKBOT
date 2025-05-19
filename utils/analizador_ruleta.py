def analizar_patron_ruleta(secuencia):
    # Lógica sencilla por ahora: muchos rojos seguidos
    rojos = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
    ultimos = secuencia[-7:]
    cantidad_rojos = sum(1 for num in ultimos if num in rojos)
    if cantidad_rojos >= 6:
        return f"¡ALERTA! 6 de los últimos 7 números son ROJOS – podés ir por el NEGRO ahora."
    return None
