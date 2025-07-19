salario_CEO = int(input("Ingrese el salario del CEO: "))
print("Salario del CEO: " + str(salario_CEO)) #se puede usar funcion str() para convertir un valor en string

salario_gerente = int(input("Ingrese el salario del gerente: "))
print("Salario del gerente: " + str(salario_gerente))#se puede usar funcion str() para convertir un valor en string

salario_supervisor = int(input("Ingrese el salario del supervisor: "))
print("Salario del supervisor: " + str(salario_supervisor))#se puede usar funcion str() para convertir un valor en string

salario_administrador = int(input("Ingrese el salario del admin: "))
print("Salario del admin: " + str(salario_administrador))#se puede usar funcion str() para convertir un valor en string

#Validar si el orden de los salarios es el correcto para una empresa
if salario_administrador<salario_supervisor<salario_gerente<salario_CEO:
    print("El orden de salarios es correcto.")
else:
    print("El orden de salarios no es el logico.")