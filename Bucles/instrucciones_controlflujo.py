#Utilizar la instruccion coninue para saltar a la siguiente iteracion del bucle
for letra in "Python":
    if letra=="y": #Si la letra es "y" se salta la iteracion actual
        continue
    
    print(f"Letra actual: {letra}")


#Contar caracteres ignorando espacios en oraciones
nombre = "Hermes Rojas Sancho"
contador=0

for caracter in nombre:
    if caracter == " ":
        continue
    contador+=1

print(f"La oracion tiene {contador} caracteres.")

#**NOTA: ctrl+c puede ayudar a salir de un bucle en un programa**
#Instruccion pass no hace nada, para cuando se necesita codigo pero ninguna instruccion

class mi_clase:
    pass #Clase que se implementara luego

def calcular():
    pass #funcion que se implementara luego


#Utilizar un else junto con un bucle for o while
email = input("Introduzca su correo: ")

for caracter in email:
    if caracter == "@":
        arroba = True
        break #este break hace que al encontrar una arroba el ELSE no se ejecute
#las instrucciones dentro de ELSE se ejecutan cuando terminan todas las iteraciones del FOR
else: #NOTAR QUE ELSE ES DEL FOR
    arroba = False

print(arroba)