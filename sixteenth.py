'''16. Conversor de Continentes'''

# Descripción: Un programa que toma el nombre de un país y devuelve a qué continente pertenece.

def obtener_continente(pais):
    continentes = {
        "África": ["Nigeria", "Sudáfrica", "Egipto", "Etiopía"],
        "Asia": ["China", "India", "Japón", "Corea del Sur"],
        "Europa": ["Alemania", "Francia", "Reino Unido", "Italia"],
        "América del Norte": ["Estados Unidos", "Canadá", "México"],
        "América del Sur": ["Brasil", "Argentina", "Chile", "Colombia"],
        "Oceanía": ["Australia", "Nueva Zelanda", "Fiyi", "Papúa Nueva Guinea"]
    }

    for continente, paises in continentes.items():
        if pais in paises:
            return continente
    return "Pais no encontrado en la base de datos"

pais = input("Ingresa el nombre de un pais: ").capitalize()
continente = obtener_continente(pais)
print(f"El {pais} está en {continente}")