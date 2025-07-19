#Funcion que evalua notas de alumnos
def evaluar_nota(nota):
    valoracion = "Aprobado"
    #Condicional if utilizado
    if nota < 7:
        valoracion="Reprobado"
    return valoracion
    

print("Programa para evaluar notas de alumnos")
nota_alumno = input("Introduzca la nota obtenida por el alumno: ") #Los datos leidos por Input siempre se convierten en STRING
print(evaluar_nota(int(nota_alumno))) #int() convierte la variable en entero 

