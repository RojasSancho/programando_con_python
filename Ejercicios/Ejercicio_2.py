#Respuesta Ejercicio 2 Pildoras Informaticas
# Crea un programa que pida por teclado “Nombre”, “Dirección” y “Tfno”. Esos tres datos 
# deberán ser almacenados en una lista y mostrar en consola el mensaje: “Los datos 
# personales son: nombre apellido teléfono” (Se mostrarán los datos introducidos por 
# teclado).

nombre = input("Ingrese su nombre: ")
direccion = input("Ingrese su direccion: ")
telefono = input("Ingrese su numero de telefono: ")

datos = [nombre, direccion, telefono]

print("Los datos personales son: " + datos[0] + ", " + datos[1] + ", " + datos[2])
