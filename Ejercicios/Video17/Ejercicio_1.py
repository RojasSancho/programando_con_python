# Ejercicio 1: 
# • Crea un programa que pida números infinitamente. Los números introducidos deben 
# ser cada vez mayores El programa finalizará cuando se introduce un número menor que 
# el anterior.

numero1 = int(input("Introduzca un numero: ")) #9
numero2 = int(input("Introduzca el siguiente numero: ")) #6

while numero2>numero1:
    numero1 = numero2
    numero2 = int(input("Introduzca el siguiente numero: "))

print("El numero ingresado es menor que el anterior. El programa ha finalizado.")