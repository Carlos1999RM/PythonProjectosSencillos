import matplotlib.pyplot as plt

# Datos de ejemplo
meses = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]
ventas = [1500, 1700, 1600, 1800, 1900, 2000, 2200, 2100, 2300, 2500, 2400, 2600]

# Crear el gráfico
plt.figure(figsize=(10,6))
plt.plot(meses, ventas, marker='o', color='b', linestyle='-', linewidth=2, markersize=6)

# Añadir títulos y etiquetas
plt.title("Ventas Mensuales en el Último Año")
plt.xlabel("Meses")
plt.ylabel("Ventas ($)")
plt.grid(True) # Añadir cuadrícula para mejor visualización

# Mostrar el gráfico
plt.show()