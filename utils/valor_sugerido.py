def calcular_valor_apuesta(nivel_confianza):
    """
    Recibe nivel_confianza (int del 1 al 5) y devuelve el valor en pesos
    """

    tabla_valores = {
        1: 2000,
        2: 5000,
        3: 10000,
        4: 20000,
        5: 50000,
    }

    return tabla_valores.get(nivel_confianza, 5000)  # valor por defecto
