#estaciones es una variable que va tomando los valores de la lista recorrida
for estaciones in ["Verano", "Invierno", "Otono", "Primavera"]: #Recorre una lista
    print(estaciones)

#utilizar range() para asimilar a un for de otros lenguajes
for i in range(5): #crea una "lista" que va de 0 a 4
    print(i)

#Validar correo (corregir y perfeccionar a mi manera)
contador=0
email=input("Introduzca su email: ")    

for i in email:
    if(i=="." or i=="@"):
        contador+=1

if contador==2:
    print("El email es valido", end=" ") #el parametro end introduce un caracter al final del print y hace que no haya salto de linea
else:
    print("El email es invalido", end=" ") #el parametro end introduce un caracter al final del print y hace que no haya salto de linea      

