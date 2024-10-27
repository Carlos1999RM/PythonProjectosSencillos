'''11. Verificador de Palíndromos'''
# Descripción: Un programa que verifica si una palabra o frase es un palíndromo (se lee igual de adelante hacia atrás).
def es_palíndromo(frase):
    frase = frase.replace(" ", "").lower()
    return frase == frase[::-1]

frase = input("Ingresa una palabra o frase: ")
if es_palíndromo(frase):
    print("Es un palíndromo")
else:
    print("No es un palíndromo")