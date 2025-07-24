#Uso de raise para lanzar excepcionces
def evaluaEdad(edad):
    if edad<0:
        raise TypeError("No se permiten edades negativas") #Lanza una excepcion TypeError con un mensaje personalizado (se pueden crear propias usando clases)
    elif edad<20:
        return "Eres bastante joven"
    elif edad<40:
        return "Eres adulto joven"
    elif edad<65:
        return "Eres un adulto maduro"
    elif edad<100:
        return "Eres un adulto mayor"

print(evaluaEdad(15))

#Lanzar excepcion con raise y capturarla
import math

def calcularRaiz(numero):
    if numero<0:
        raise ValueError("El numero no puede ser negativo.")
    else:
        return math.sqrt(numero)

numero1 = int(input("Ingrese el numero: "))

try:
    print(calcularRaiz(numero1))
except ValueError as error_numero_negativo: 
    print(error_numero_negativo)

print("Programa finalizado.")