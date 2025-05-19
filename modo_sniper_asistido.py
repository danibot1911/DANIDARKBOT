import requests
from utils.generador_voz_paisa import generar_audio
from templates.boton_generator import crear_boton
from analizador_ruleta import analizar_patron_ruleta

def ejecutar_modo_sniper(datos, telegram):
    secuencia = datos.get("resultados", [])
    if not secuencia:
        return

    mensaje, nivel = analizar_patron_ruleta(secuencia)

    if mensaje:
        texto_final = ""
        if nivel == 1:
            texto_final = "Parce… eso está frío, no te calientes todavía. Si querés, mete algo suave pa tantear."
        elif nivel == 2:
            texto_final = "Esta pinta buena, mi amor. Si estás en mood de hacer plata, metele unos diez luquitas sin miedo."
        elif nivel == 3:
            texto_final = "Ay mijo… esto está para cobrar. Meté esos 20 o 50 si te da la cabeza, porque esta no se repite."
        elif nivel == 4:
            texto_final = "Oíme bien… esta jugada es una joya. Si tenés con qué, meté todo. Esas no vuelven, bebé."

        voz_path = generar_audio(texto_final)
        boton = crear_boton("Abrir RushBet ya pues", "https://www.rushbet.co/casino/live")

        telegram.enviar_mensaje_completo(
            texto=f"**DANY SNIPER PAISA – NIVEL {nivel}**\n\n{mensaje}\n\n{texto_final}",
            botones=[boton],
            audio=voz_path
        )
