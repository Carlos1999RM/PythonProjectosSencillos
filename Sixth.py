'''6. Agenda de Contactos'''
# Descripción: Un programa que permite almacenar, buscar y eliminar contactos.
contactos = {}

def agregar_contacto(nombre, teléfono):
    contactos[nombre] = teléfono

def buscar_contacto(nombre):
    return contactos.get(nombre, "Contacto no encontrado")

def eliminar_contacto(nombre):
    if nombre in contactos:
        del contactos[nombre]
        print(f"Contacto {nombre} eliminado.")
    else:
        print("Contacto no encontrado")

while True:
    print("1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Eliminar contacto")
    print("4. Salir")
    opción = input("Elige una opción: ")

    if opción == '4':
        break
    elif opción == '1':
        nombre = input("Nombre: ")
        teléfono = input("Teléfono: ")
        agregar_contacto(nombre, teléfono)
    elif opción == '2':
        nombre = input("Nombre: ")
        print(buscar_contacto(nombre))
    elif opción == '3':
        nombre = input("Nombre: ")
        eliminar_contacto(nombre)
    else:
        print("Opción no válida")