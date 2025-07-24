#Realizando una funcion tradicional que genera numeros pares hasta un limite
def funcion_genera_pares (limite):
    num=1
    lista =[]
    
    while num<=limite:
        lista.append(num*2)
        num+=1
    return lista

print(funcion_genera_pares(10))

#Generador que hace lo mismo
def generador_pares(limite):
    num=1
    
    while num<=limite:
        yield num*2
        num+=1

devuelve_pares = generador_pares(10) #Creando una variable con objeto del generador

# for numero_generado in devuelve_pares: #Recorre generador numero a numero, sin generar aun los siguientes
#     print(numero_generado)

#Utilizar instruccion next para ir generando de uno en uno

print(f"\n{next(devuelve_pares)}")

print("Muchas lineas de codigo mas...")

print(next(devuelve_pares))

print("Muchas lineas de codigo mas...")

print(next(devuelve_pares))

print("Muchas lineas de codigo mas...")