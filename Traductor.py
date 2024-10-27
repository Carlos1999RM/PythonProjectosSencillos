from googletrans import Translator, LANGUAGES

# Crear instancia del traductor
translator = Translator()

def traducir_texto(texto, idioma_destino):
    """
    Traduce el texto al idioma especificado.

    Parámetros:
    texto (str): El texto a traducir.
    idioma_destino (str): Código del idioma al cual traducir (ej. 'es' para español, 'en' para inglés).

    Retorna:
    str: Texto traducido.
    """
    # Detecta el idioma original
    deteccion = translator.detect(texto)
    idioma_origen = deteccion.lang
    print(f"Idioma detectado: {LANGUAGES.get(idioma_origen, 'desconocido')} ({idioma_origen})")

    # Traduce el texto
    tradccion = translator.translate(texto, dest=idioma_destino)
    print(f"Traducción al {LANGUAGES.get(idioma_destino, 'desconocido')}: ")
    return tradccion.text
    
# Ejemplo de uso
texto_a_traducir = "Hola, hacia dónde vas?"
idioma_destino = 'en' # Cambiar el código según el idioma deseado
traduccion = traducir_texto(texto_a_traducir, idioma_destino)
print(traduccion)