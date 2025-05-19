from templates.boton_generator import generar_boton_apuesta
from utils.analizador_ruleta import analizar_patron_ruleta

def ejecutar_modo_sniper(datos, telegram):
    secuencia = datos.get("resultados", [])
    if not secuencia:
        return "Sin datos de secuencia."

    mensaje = analizar_patron_ruleta(secuencia)

    if mensaje:
        nivel = 1
        if "6" in mensaje:
            nivel = 1
        elif "7" in mensaje:
            nivel = 2
        elif "8" in mensaje:
            nivel = 3
        elif "9" in mensaje:
            nivel = 4

        texto_final = ""
        if nivel == 1:
            texto_final = "Parce… eso está fresco, pero pilas."
        elif nivel == 2:
            texto_final = "Esta pinta buena, vamos subiendo de nivel."
        elif nivel == 3:
            texto_final = "Ay mijo… esto está candela, pa' que sepa."
        elif nivel == 4:
            texto_final = "Óime bien… esta jugada está que revienta billete."

        texto_alerta = f"{texto_final}\n\n{mensaje}"
        boton = generar_boton_apuesta("Ir a RushBet", "https://www.rushbet.co")

        if telegram:
            telegram.enviar_mensaje_completo(
                texto=f"**DANY SNIPER PAISA — NIVEL {nivel}**\n\n{texto_alerta}",
                botones=[boton],
            )

        return f"Alerta enviada: {texto_alerta}"

    return "Sin patrón claro para alerta."
