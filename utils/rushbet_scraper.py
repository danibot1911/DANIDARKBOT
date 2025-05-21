import random

def obtener_numeros_ruleta():
    """
    Simula la obtención de los últimos 20 resultados de una ruleta.
    En una versión real, aquí se conectaría a una API o se haría scraping a Rushbet.
    """
    # Simulación: genera 20 números aleatorios entre 0 y 36
    resultados = [random.randint(0, 36) for _ in range(20)]
    print(f"[SCRAPER] Últimos números simulados: {resultados}")
    return resultados
