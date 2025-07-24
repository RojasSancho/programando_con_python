#Definir una funcion
def mensaje(): #En los parentesis se pueden colocar parametros opcionales 
    
    #Instrucciones de la funcion
    print("Hola, estoy aprendiendo a usar funciones en Python")
    print("Este es un segundo mensaje")
    print("Voy a volverme un toro en esto!")
    
    #Opcionalmente se puede retornar un valor
    
def suma(numero1, numero2):
    return numero1 + numero2

#Ejecutar las funciones                                          
mensaje() #colocar parametros si es necesario

print(suma(540, 60))
