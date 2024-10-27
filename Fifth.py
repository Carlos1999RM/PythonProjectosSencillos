'''5. Contador de Palabras'''
# Descripción: Un programa que cuenta la cantidad de palabras en una frase.
def contar_palabras(frase):
    palabras = frase.split()
    return len(palabras)

frase = input("Ingresa una frase: ")
print(f"La frase tiene {contar_palabras(frase)} palabras.")