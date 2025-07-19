print("Verificacion de acceso por edad")

edad = int(input("Ingrese su edad, por favor: ")) #int() hace que el valor recibido por input() se convierta en entero

if edad<18:
    print("Eres menor de edad, no tienes permitido ingresar.")
elif edad<65: #else if:
    print("Eres un adulto, puedes ingresar.")
else: #entra al else solo si todo lo anterior no se cumple
    print("Eres un adulto mayor, puedes ingresar.")
    
