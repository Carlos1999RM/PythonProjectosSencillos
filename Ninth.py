'''9. Calculadora de IMC (Índice de Masa Corporal)'''
# Descripción: Calcula el IMC de una persona en función de su peso y altura.
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

peso = float(input("Ingresa tu peso en kg: "))
altura = float(input("Ingresa tu altura en metros: "))
imc = calcular_imc(peso, altura)

print(f"Tú IMC es {imc:.2f}")

if imc < 18.5:
    print("Bajo peso")
elif 18.5 <= imc < 24.9:
    print("Peso normal")
elif 25 <= imc < 29.9:
    print("Sobrepeso")
else:
    print("Obesidad")