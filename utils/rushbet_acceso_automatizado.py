
import requests
from bs4 import BeautifulSoup

RUSHBET_RULETA_URL = "https://www.rushbet.co/?page=casino&category=live"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X)"
}

def analizar_rushbet():
    try:
        response = requests.get(RUSHBET_RULETA_URL, headers=HEADERS)
        soup = BeautifulSoup(response.content, "html.parser")
        posibles_numeros = []

        for span in soup.find_all("span"):
            texto = span.get_text().strip()
            if texto.isdigit() and 0 <= int(texto) <= 36:
                posibles_numeros.append(int(texto))

        if posibles_numeros:
            print(f"[RUSHBET] Números capturados: {posibles_numeros}")
            return posibles_numeros
        else:
            print("[RUSHBET] No se detectaron números")
            return []

    except Exception as e:
        print(f"[ERROR] al obtener datos de la ruleta: {e}")
        return []
