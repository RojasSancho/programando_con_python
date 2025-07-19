#Respuesta Ejercicio 1 Pildoras Informaticas
# Crea un programa que pida dos números por teclado. El programa tendrá una función 
# llamada “DevuelveMax” encargada de devolver el número más alto de los dos 
# introducidos. 

def devuelve_max (numero1, numero2):
    if numero1>numero2:
        return numero1
    else:
        return numero2
        

numero1 = int(input("Ingrese el primer numero a comparar: "))
numero2 = int(input("Ingrese el segundo numero a comparar: "))
if numero2==numero1:
    numero2 = int(input("Ingrese un numero diferente al primero: ")) #lo mejor seria utilizar un bucle
    
numero_mayor = devuelve_max(numero1, numero2)
    
print(f"El numero mas alto es: {numero_mayor}") #usando un f-string (MUY UTIL)

