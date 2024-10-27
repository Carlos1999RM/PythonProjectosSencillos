'''7. Conversor de Monedas'''
# Descripción: Un programa que convierte entre diferentes monedas usando tasas de cambio predeterminadas.
def convertir_moneda(cantidad, tasa_cambio):
    return cantidad * tasa_cambio

print("Conversor de monedas")
print("1. USD a EUR")
print("2. EUR a USD")

opción = input("Elige una opción: ")

if opción == '1':
    cantidad = int(input("Cantidad en USD: "))
    tasa_cambio = 0.92 # Ejemplo de tasa de cambio
    print(f"{cantidad} USD son {convertir_moneda(cantidad, tasa_cambio)} EUR")
elif opción == '2':
    cantidad = int(input("Cantidad en EUR: "))
    tasa_cambio = 1.09 # Ejemplo de tasa de cambio
    print(f"{cantidad} EUR son {convertir_moneda(cantidad, tasa_cambio)} USD")
else:
    print("Opción no válida")