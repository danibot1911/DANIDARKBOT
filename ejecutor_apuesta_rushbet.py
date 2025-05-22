from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def ejecutar_apuesta():
    print("Iniciando apuesta automática en RushBet...")

    options = Options()
    options.add_argument('--headless')  # sin navegador visible
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')

    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://www.rushbet.co")
        time.sleep(5)

        # Clic en "Iniciar sesión"
        login_btn = driver.find_element(By.XPATH, '//button[contains(text(), "Iniciar sesión")]')
        login_btn.click()
        time.sleep(3)

        # Rellenar usuario y contraseña
        driver.find_element(By.NAME, "email").send_keys("andresgot11@gmail.com")
        driver.find_element(By.NAME, "password").send_keys("Emidaso19$")
        driver.find_element(By.XPATH, '//button[contains(text(), "Iniciar sesión")]').click()
        time.sleep(6)

        # Ir a la ruleta directamente
        driver.get("https://www.rushbet.co/?page=all-games&game=225")
        time.sleep(6)

        # Aquí deberíamos localizar y hacer clic en el botón de apuesta
        # Pero como RushBet es en vivo, este paso es altamente dinámico
        # Lo dejamos como print simulado por ahora

        print("✅ Apuesta ejecutada (simulada) en ruleta RushBet")

    except Exception as e:
        print(f"❌ Error durante la ejecución automática: {e}")

    finally:
        driver.quit()
