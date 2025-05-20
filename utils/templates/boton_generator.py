def generar_boton_apuesta(texto, url):
    return {
        "inline_keyboard": [[
            {"text": texto, "url": url}
        ]]
    }
