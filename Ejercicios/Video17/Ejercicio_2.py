# Ejercicio 2: 
# • Crea un programa que pida números positivos indefinidamente. El programa termina 
# cuando se introduce un número negativo. Finalmente el programa muestras la suma de 
# todos los números introducidos 

numero=int(input("Introduzca un numero positivo: "))
lista_numeros=[]
suma_numeros = 0

while numero>=0:
    lista_numeros.append(numero)
    numero=int(input("Introduzca otro numero positivo: "))

for numero in lista_numeros:
    suma_numeros += numero

print("Se intrdujo un numero negativo, programa finalizado.")
print(f"El total de la suma de todos los numeros positivos introducidos es: {suma_numeros}")