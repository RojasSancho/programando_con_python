#Generador de ciudades con for anidado (devuelve las letras de las ciudades)
def devuelve_ciudades(*ciudades): #el "*" hace que se le puedan pasar varios parametros al generador
    for ciudad in ciudades:#recorre la lista de ciudades
        for caracter in ciudad: #recorre cada caracter de la ciudad actual
            yield caracter #genera la letra

ciudades_devuelta = devuelve_ciudades("San Jose", "Alajuela", "Cartago", "Heredia")

#Generando las primeras tres letras de la primer ciudad
print(next(ciudades_devuelta))
print(next(ciudades_devuelta))
print(next(ciudades_devuelta))

#Generador de ciudades usando YIELD FROM
def devuelve_ciudades(*ciudades): #el "*" hace que se le puedan pasar varios parametros al generador
    for ciudad in ciudades: #recorre la lista de ciudades
        #for caracter in ciudad: #recorre cada caracter de la ciudad actual
        yield from ciudad #entra en la ciudad para generar cada caracter

ciudades_devuelta = devuelve_ciudades("San Jose", "Alajuela", "Cartago", "Heredia")

#Generando las primeras tres letras de la primer ciudad
print(next(ciudades_devuelta))
print(next(ciudades_devuelta))
print(next(ciudades_devuelta))
