for i in range(5, 50, 3): #range(inicio del rango, final del rango-1, patron a utilizar para el conteo)
    print(f"Valor de la variable: {i}") #usando f-string para combinar string con enteros en print


#Ejemplo de bucle for usando la funcion len()
valido=False
email=input("Ingrese su correo: ")

for i in range(len(email)): #crea un rango del largo del email ingresado
    if email[i] == "@": #recorre cada char del email para verificar si es @
        valido=True
