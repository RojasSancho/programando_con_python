#Trabajando con diccionarios
#Pueden almacenar todo tipo de datos, incluso listas y otros diccionarios
#A cada valor se le asigna una clave unica (las claves NO se pueden repetir)
#No existe orden en los diccionarios, da igual

#1 - Sintaxis de un diccionario
mi_diccionario = {"Alemania":"Berlin", "Francia":"Paris", "Reino Unido":"Londres", "Espana":"Madrid"} 

#2 - Imprimir un valor de un diccionario
print(mi_diccionario["Alemania"]) #Imprime madrid (Espana es la clave)

#3 - Imprimir diccionario completo
print(mi_diccionario)

#4 - Anadir un valor mas al diccionario
mi_diccionario["Italia"] = "Lisboa"

#5 - Modificar el valor a una clave (corregir)
mi_diccionario["Italia"] = "Roma"

#6 - Eliminar una clave y su valor de un diccionario
del mi_diccionario["Espana"]

#7 - Crear un diccionario con varios tipos de variable
diccionario_mixto = {"Francia":"Paris", 23:"M.Jordan", "Mosqueteros":3}
print(diccionario_mixto)

#8 - Usar tupla para asignar claves a un diccionario
tupla = ("Josue", "Miguel", "Flori")
diccionario2 = {tupla[0]:23, tupla[1]:35, tupla[2]:45}
print(diccionario2["Josue"]) #O print(diccionario2[tupla[0]])

#9 - Diccionario almacenando una tupla
diccionario_contupla = {23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago Bulls", "Anillos":(1991,1992,1993,1996,1997,1998)}
print(diccionario_contupla["Anillos"])

#10 - Diccionario dentro de otro diccionario
diccionario_dentrode_diccionario = {23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago Bulls", "Anillos":{"Temporadas":(1991,1992,1993,1996,1997,1998)}}
print(diccionario_dentrode_diccionario["Anillos"])

#11 - Metodos importantes extra de diccionarios

#Devuelve solo las claves de un diccionario
print(diccionario_dentrode_diccionario.keys())

#Devuelve solo los valores de un diccionario
print(diccionario_dentrode_diccionario.values())

#Devuelve la longitud o tamano del diccionario
print(len(diccionario_dentrode_diccionario))