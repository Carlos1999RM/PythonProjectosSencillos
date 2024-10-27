'''10. Creador de Acrónimos'''
# Descripción: Un programa que toma una frase y genera un acrónimo a partir de las primeras letras de cada palabra.
def crear_acrónimo(frase):
    words = frase.split()
    acrónimo = ''.join([word[0].upper() for word in words])
    return acrónimo
frase = input("Ingresa una frase: ")
print(f"El acrónimo es: {crear_acrónimo(frase)}")