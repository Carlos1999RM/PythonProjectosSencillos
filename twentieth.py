# ejemplo completo que incluye una clase principal y una clase derivada:
'''
Buenas Prácticas
Encapsulación: Usa métodos para acceder y modificar atributos en lugar de acceder directamente a los atributos.

Documentación: Añade comentarios y docstrings a tus clases y métodos para describir su propósito y cómo se deben usar.

Pruebas: Es útil escribir pruebas para verificar que tus clases y métodos funcionen correctamente.
'''
class CazaCombate:
    def __init__(self, modelo, capacidad):
        self.modelo = modelo
        self.capacidad = capacidad
    
    def descripcion(self):
        return f"Vehículo aéreo: {self.modelo} {self.capacidad}"
    
class CazaBombardero(CazaCombate):
    def __init__(self, modelo, capacidad, año):
        super().__init__(modelo, capacidad)
        self.año = año

    def descripcion(self):
        return f"Caza bombardero: {self.modelo} {self.capacidad} Año: {self.año}"

# Crear instancias
caza = CazaCombate("Caza de superioridad aérea Mikoyan", "Mig-35")
cazaBombardero = CazaBombardero("Sukhoi", "Su-34", "1990")

print(caza.descripcion())
print(cazaBombardero.descripcion())
