#Solicitar un edad valida (WHILE)
edad=int(input("Introduzca su edad: "))

while edad<1 or edad>150: #hace que no se salga del bucle hasta que se cumpla la condicion (PUEDE PRODUCIRSE UN BUCLE INFINITO)
    print("La edad introducida no es valida, vuelva a intentarlo")
    edad=int(input("Introduzca su edad: "))

print(f"El programa ha finalizado. Edad del aspirante: {edad}") #usando f-string

#Utilizar la clase math y utilizar break para salir de un bucle while
import math
print("\nPrograma para calcular raiz cuadrada de un numero natural")
numero=int(input("Ingrese su numero: "))

intentos=0

while numero<0:
    if intentos == 3:
        print("Ha hecho demasiados intentos. El programa finalizara.")
        break
    
    print("No es posible calcular raiz cuadrada de un numero negativo.")
    numero = (int(input("Ingrese un numero valido: ")))
    intentos +=1
    
if numero>=0:
    raiz_cuadrada = math.sqrt(numero)
    print(f"La raiz cuadrada de {numero} es {raiz_cuadrada}")