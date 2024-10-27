'''12. Conversor de Número a Palabras'''
# Descripción: Convierte un número (como 123) a su equivalente en palabras (como "ciento veintitrés").
def números_a_palabras(num):
    unidades = ["cero", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"]
    decenas = ["", "", "veinte", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa"]
    especiales = ["diez", "once", "doce", "trece", "catorce", "quince", "dieciséis", "diecisiete", "dieciocho", "diecinueve"]

    if 0 <= num < 10:
        return unidades[num]
    elif 10 <= num < 10:
        return especiales[num-10]
    elif 20 <= num < 100:
        if num % 10 == 0:
            return decenas[num//10]
        else:
            return decenas[num//10] + " y " + unidades[num%10]
    else:
        return "Número fuera de rango"
    
números = int(input("Ingresa un número (0-99): "))
print(números_a_palabras(números))