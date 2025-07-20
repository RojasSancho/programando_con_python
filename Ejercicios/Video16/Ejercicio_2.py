# Ejercicio 2: 
# • Crea un programa que pida por teclado introducir una contraseña. La contraseña no 
# podrá tener menos de 8 caracteres ni espacios en blanco. Si la contraseña es correcta, 
# el programa imprime “Contraseña OK”. En caso contrario imprime “Contraseña 
# errónea” 

contrasena_usuario = input("Ingrese su nueva contrasena: ")
validez=True

if len(contrasena_usuario) < 8:
    validez=False

for caracter in contrasena_usuario:
    if caracter==" ":
        validez=False

if validez==True:
    print("Contrasena OK")
else:
    print("Contrasena erronea")

