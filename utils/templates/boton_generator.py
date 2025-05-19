def generar_boton_apuesta(texto_boton="Ir a RushBet", url="https://www.rushbet.co"):
    return {
        "inline_keyboard": [[
            {"text": texto_boton, "url": url}
        ]]
    }
