'''14. Reversor de Texto'''
# Descripción: Un programa que toma una palabra o frase y la muestra al revés.
def reversar_texto(texto):
    return texto[::-1]
texto = input("Ingresa una palabra o frase: ")
print(f"El texto al revés es: {reversar_texto(texto)}")