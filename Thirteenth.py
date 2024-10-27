'''13. Contador de Vocales'''
# Descripción: Un programa que cuenta cuántas vocales hay en una palabra o frase ingresada por el usuario.

def contar_vocales(frase):
    vocales = "aeiouAEIOU"
    contador = 0
    for letra in frase:
        if letra in vocales:
            contador += 1
    return contador

frase = input("Ingresa una palabra o frase: ")
print(f"Hay {contar_vocales(frase)} vocales en la frase.")