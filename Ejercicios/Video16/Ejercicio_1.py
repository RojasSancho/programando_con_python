# Ejercicio 1: 
# • Crea un programa que muestre los números impares del 1 al 100. Los números deberán 
# aparecer una al lado del otro sin salto de línea. 

for i in range(1, 101):
    sobrante=i%2
    if sobrante!=0:
        print(i,end=" ")
    