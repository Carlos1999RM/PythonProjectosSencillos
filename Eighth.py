'''8. Juego de Piedra, Papel o Tijeras'''
# Descripción: Un juego clásico donde el usuario juega contra la computadora.
import random

opciones = ["piedra", "papel", "tijeras"]

def game():
    user = input("Elige piedra, papel o tijeras: ").lower()
    ordenador = random.choice(opciones)
    print(f"El ordenador eligió: {ordenador}")

    if user == ordenador:
        return "¡Empate!"
    elif (user == "piedra" and ordenador == "tijeras") or \
         (user == "papel" and ordenador == "piedra") or \
         (user == "tijeras" and ordenador == "papel"):
        return "¡Ganaste!"
    else:
        return "¡Perdiste!"
    
while True:
    resultado = game()
    print(resultado)
    jugar_de_nuevo = input("¿Quieres jugar de nuevo? (s/n): ").lower()
    if jugar_de_nuevo != 's':
        break