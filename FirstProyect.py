'''1. Calculadora Básica'''
# Descripción: Crea una calculadora que pueda realizar operaciones básicas como suma, resta, multiplicación y división.
def suma(a, b):
    return a + b
def resta(a, b):
    return a - b
def multiplicación(a, b):
    return a * b
def división(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "No se puede dividir por cero"

while True:
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")
    opción = input("Elige una operación: ")

    if opción == '5':
        break

    num_1 = int(input("Ingrese el primer número: "))
    num_2 = int(input("Ingrese el segundo número: "))

    if opción == '1':
        print(f"Resultado de la suma: {suma(num_1, num_2)}")
    elif opción == '2':
        print(f"Resultado de la resta: {resta(num_1, num_2)}")
    elif opción == '3':
        print(f"Resultado de la multiplicación: {multiplicación(num_1, num_2)}")
    elif opción == '4':
        print(f"Resultado de la división: {división(num_1, num_2)}")
    else:
        print("Opción no válida")