import requests
from bs4 import BeautifulSoup

# URL directa a la ruleta elegida (personalizada con el juego específico)
RUSHBET_RULETA_URL = "https://www.rushbet.co/?page=all-games&game=225"

# Simula cabecera de navegador
HEADERS = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15A372 Safari/604.1"
}

def obtener_numeros_ruleta():
    try:
        response = requests.get(RUSHBET_RULETA_URL, headers=HEADERS)
        soup = BeautifulSoup(response.content, "html.parser")

        # Aquí busca en el HTML los datos de la ruleta (esto puede variar si cambia el DOM)
        posibles_numeros = []

        for span in soup.find_all("span"):
            texto = span.get_text().strip()
            if texto.isdigit() and 0 <= int(texto) <= 36:
                posibles_numeros.append(int(texto))

        if posibles_numeros:
            print(f"[RUSHBET] Números capturados: {posibles_numeros}")
            return posibles_numeros
        else:
            print("[RUSHBET] No se detectaron números válidos")
            return []

    except Exception as e:
        print(f"[ERROR] al obtener datos de la ruleta: {e}")
        return []
