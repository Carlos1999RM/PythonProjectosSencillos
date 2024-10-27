'''15. Juego de Capitales del Mundo'''
# Descripción: Un programa que pregunta al usuario la capital de un país específico. 
# El usuario tiene que adivinar la capital, y el programa le dirá si es correcto o no.
capitales = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Canadá": "Ottawa",
    "Francia": "París",
    "Alemania": "Berlín",
    "India": "Nueva Delhi",
    "Japón": "Tokio",
    "México": "Ciudad de México",
    "España": "Madrid",
    "Estados Unidos": "Washington, D.C.",
    "Polonia": "Varsovia",
}

while True:
    pais = input("Ingresa el nombre de un país (o 'salir' para terminar): ")

    if pais.lower() == 'salir':
        break
    if pais in capitales:
        respuesta = input(f"¿Cuál es la capital de {pais}: ").capitalize()
        if respuesta == capitales[pais]:
            print("¡Correcto!")
        else:
            print(f"Incorrecto. La capital de {pais} es {capitales[pais]}.")
    else:
        print("País no encontrado en la base de datos.")