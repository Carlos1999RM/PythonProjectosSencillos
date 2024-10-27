'''Aquí tienes un ejemplo de código en Python que utiliza un bloque try...except para manejar varias excepciones posibles:'''

def calcular_division():
    try:
        numerador =int(input("Introduce el numerador (un número entero): "))
        denominador = int(input("Introduce el denominador (otro número entero): "))
        resultado = numerador / denominador
    except ValueError:
        print("Error: Debes introducir números enteros.")
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
    else:
        print(f"El resultado de la división es: {resultado}")
    finally:
        print("Gracias por usar el programa.")

# Llamamos a la función
calcular_division()

'''
¿Qué hace este código?
Ingreso de datos: Solicita al usuario que introduzca dos números enteros.
Bloque try: Intenta realizar la división de los dos números.
Manejo de excepciones:
ValueError: Si el usuario introduce algo que no es un número entero, el programa captura esta excepción y 
muestra un mensaje de error.

ZeroDivisionError: Si el usuario intenta dividir por cero, se captura la excepción y se muestra un mensaje 
indicando que no se puede realizar esa operación.

Exception: Captura cualquier otra excepción que pueda ocurrir y muestra el mensaje de error correspondiente.
Bloque else: Si no ocurre ninguna excepción, se muestra el resultado de la división.

Bloque finally: Se ejecuta siempre, independientemente de si hubo o no una excepción. En este caso, muestra un 
mensaje de agradecimiento.

Este código maneja posibles errores en la entrada del usuario y asegura que el programa no se detenga abruptamente, 
proporcionando mensajes útiles cuando algo va mal.







'''