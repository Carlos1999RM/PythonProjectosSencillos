'''Aquí tienes otro ejemplo de código en Python utilizando try...except que simula un sistema de 
acceso basado en un nombre de usuario y una contraseña:
'''

def iniciar_sesion():
    usuarios_registrados = {"usuario1": "password123", "usuario2": "qwerty", "usuario3": "12345"}

    try:
        usuario = input("Introduce tu nombre de usuario: ")
        if usuario not in usuarios_registrados:
            raise KeyError("Uusario no encontrado.")
        
        contraseña = input("Introduce tu contraseña: ")
        if usuarios_registrados[usuario] != contraseña:
            raise ValueError("Contraseña incorrecta.")
    
    except KeyError as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Ha ocurrido un error inesperado: {e}")
    else:
        print(f"Bienvenido, {usuario}!")
    finally: print("Proceso de inicio de sesión finalizado.")

# Llamamos a la función
iniciar_sesion()

'''
¿Qué hace este código?
Base de datos simulada: Define un diccionario llamado usuarios_registrados que almacena pares de nombre de usuario y contraseña.
Ingreso de datos: Solicita al usuario que introduzca su nombre de usuario y contraseña.
Bloque try:
Verifica si el nombre de usuario existe en el diccionario. Si no es así, lanza una excepción KeyError.
Verifica si la contraseña proporcionada coincide con la almacenada. Si no es así, lanza una excepción ValueError.
Manejo de excepciones:
KeyError: Captura el error si el nombre de usuario no está en la lista de usuarios registrados y muestra un mensaje adecuado.
ValueError: Captura el error si la contraseña es incorrecta y muestra un mensaje de advertencia.
Exception: Captura cualquier otro tipo de error inesperado.
Bloque else: Si el nombre de usuario y la contraseña son correctos, el usuario es bienvenido.
Bloque finally: Se ejecuta siempre, mostrando un mensaje de finalización del proceso de inicio de sesión.
Este ejemplo es útil para entender cómo manejar posibles errores en un proceso común como el inicio de sesión, garantizando que el programa no se detenga inesperadamente y proporcionando retroalimentación adecuada al usuario.









'''