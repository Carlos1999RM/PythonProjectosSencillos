'''4. Conversor de Unidades'''
# Descripción: Crea un programa que convierta entre diferentes unidades de medida (por ejemplo, metros a kilómetros, 
# grados Celsius a Fahrenheit).
def celsius_a_farenheit(celsius):
    return(celsius * 9/5) + 32

def metros_a_kilometros(metros):
    return metros / 1000

print("1. Celsius a Farenheit")
print("2. Metros a kilómetros")

opción = input("Elige una conversión: ")

if opción == '1':
    celsius = float(input("Ingresa la temperatura en celsius: "))
    print(f"{celsius} ºC = {celsius_a_farenheit(celsius)} ºF")
elif opción == '2':
    metros = float(input("Ingresa la distancia en metros: "))
    print(f"{metros} m = {metros_a_kilometros(metros)} km")
else:
    print("Opción no válida")