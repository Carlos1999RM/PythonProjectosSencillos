'''3. Generador de Contraseñas'''
# Descripción: Un programa que genera contraseñas seguras al azar.
import random
import string

def generar_contraseña(longitud):
    carácteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = ''.join(random.choice(carácteres) for _ in range(longitud))
    return contraseña

longitud = int(input("Ingresa la longitud de la contraseña:"))
print(f"Contraseña generada: {generar_contraseña(longitud)}")