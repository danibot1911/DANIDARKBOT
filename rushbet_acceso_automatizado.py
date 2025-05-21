import requests
from bs4 import BeautifulSoup
import time

# ===== DATOS DE USUARIO RushBet =====
USERNAME = "andresgot11@gmail.com"
PASSWORD = "Emidaso19$"
RUSHBET_LOGIN_URL = "https://www.rushbet.co/api/login"
RUSHBET_GAME_URL = "https://www.rushbet.co/?page=all-games&game=225"

# ===== FUNCIÓN DE ACCESO Y MONITOREO DE RULETA =====
def obtener_numeros_ruleta():
    session = requests.Session()

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Content-Type": "application/json"
    }

    # Paso 1: Iniciar sesión
    login_payload = {
        "email": USERNAME,
        "password": PASSWORD
    }

    response = session.post(RUSHBET_LOGIN_URL, json=login_payload, headers=headers)

    if response.status_code != 200:
        print("[ERROR] Falló el login a RushBet.")
        return []

    print("[OK] Sesión iniciada correctamente.")

    # Paso 2: Ir a la ruleta
    game_response = session.get(RUSHBET_GAME_URL)

    if game_response.status_code != 200:
        print("[ERROR] No se pudo acceder al juego.")
        return []

    soup = BeautifulSoup(game_response.text, 'html.parser')

    # Paso 3: Extraer los números de la ruleta
    numeros_detectados = []

    # NOTA: Este selector puede cambiar dependiendo del HTML exacto
    elementos = soup.find_all("div", class_="game-history-number")
    for elem in elementos:
        try:
            numero = int(elem.text.strip())
            numeros_detectados.append(numero)
        except:
            continue

    print(f"[RUSHBET] Números obtenidos: {numeros_detectados[:10]}")
    return numeros_detectados[:10]
