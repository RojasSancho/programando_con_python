#Ejemplo de utilizar varios except consecutivos en un mismo try
def divide():
    try:
        numero1=(float(input("Introduce el primer numero: ")))
        numero2=(float(input("Introduce el segundo numero: ")))
        
        print(f"La division da: {numero1/numero2}")
    except ValueError:
        print("El valor introducido es incorrecto.")    
    except ZeroDivisionError:    
        print("No es posible dividir entre cero.")
    
    #lo que vaya dentro del finally se ejecuta siempre, haya excepcion o no (sirve para cuando se usen Bases de Datos)
    finally:
        print("Calculo hecho.")

#Usar un try solo con un finally, aunque lo del try genere error se ejecuta el finally
def divide2():
    try:
        numero1=(float(input("Introduce el primer numero: ")))
        numero2=(float(input("Introduce el segundo numero: ")))
        
        print(f"La division da: {numero1/numero2}")
    #lo que vaya dentro del finally se ejecuta siempre, haya excepcion o no (sirve para cuando se usen Bases de Datos)
    finally:
        print("Calculo hecho.")

#Usar un solo except para atrapar todas las excepciones, de formas mas general
def divide3():
    try:
        numero1=(float(input("Introduce el primer numero: ")))
        numero2=(float(input("Introduce el segundo numero: ")))
        
        print(f"La division da: {numero1/numero2}")
    except:
        print("Ha ocurrido un error en la ejecucion.")    
    
    print("Funcion finalizada.")

