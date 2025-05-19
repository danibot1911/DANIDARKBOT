import os
import uuid
import pyttsx3

def generar_audio(texto):
    ruta_base = "voz"
    if not os.path.exists(ruta_base):
        os.makedirs(ruta_base)

    nombre_archivo = f"{uuid.uuid4().hex}.mp3"
    ruta_completa = os.path.join(ruta_base, nombre_archivo)

    engine = pyttsx3.init()
    engine.setProperty("rate", 175)  # velocidad de habla
    engine.setProperty("volume", 1.0)  # volumen máximo

    # Voz femenina paisa si está disponible
    voces = engine.getProperty("voices")
    for voz in voces:
        if "female" in voz.name.lower() or "spanish" in voz.name.lower():
            engine.setProperty("voice", voz.id)
            break

    engine.save_to_file(texto, ruta_completa)
    engine.runAndWait()

    return ruta_completa
