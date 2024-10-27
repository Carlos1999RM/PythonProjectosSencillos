'''17. Banderas de Colores'''

# Descripción: Un programa que toma el nombre de un país y devuelve los colores principales de su bandera.

def obtener_colores_bandera(pais):
    banderas = {
         "Argentina": ["Celeste", "Blanco"],
        "Brasil": ["Verde", "Amarillo", "Azul", "Blanco"],
        "Canadá": ["Rojo", "Blanco"],
        "Francia": ["Azul", "Blanco", "Rojo"],
        "Alemania": ["Negro", "Rojo", "Amarillo"],
        "India": ["Azafrán", "Blanco", "Verde"],
        "Japón": ["Blanco", "Rojo"],
        "México": ["Verde", "Blanco", "Rojo"],
        "España": ["Rojo", "Amarillo"],
        "Estados Unidos": ["Rojo", "Blanco", "Azul"]
    }

    return banderas.get(pais, "Pais no encontrado en la base de datos")

pais = input("Ingresa el nombre de un pais: ").capitalize()
colores = obtener_colores_bandera(pais)

if isinstance(colores, list):
    print(f"Los colores de la bandera de {pais} son: {', '.join(colores)}")
else:
    print(colores)