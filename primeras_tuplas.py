#Primeras tuplas (listas inmutables)
#NO SE PUEDEN MODIFICAR (NO USAR APPEND, NI EXTEND, NI INSERT, ETC)
#**SI SE PUEDE USAR INDEX PARA BUSCAR ELEMENTOS**

#1 - Sintaxis de una tupla
primera_tupla = (1, 2, 3, 4, 5, 3)

#2 - Devolver un elemento de un indice concreto de la tupla
print(primera_tupla[2])

#3 - Convertir una tupla en una lista
lista_desdetupla = list(primera_tupla)
print(lista_desdetupla)

#4 - Convertir una lista en una tupla
tupla_desdelista = tuple(lista_desdetupla)
print(tupla_desdelista)

#5 - Verificar si un elemento se encuentra en una tupla
print(4 in tupla_desdelista) #Devuelve boolean

#6 - Contar cuantas veces se repite un elemento en la tupla
print(tupla_desdelista.count(3))   

#7 - Consultar longitud o tamano de una tupla
print(len(tupla_desdelista))

#8 - Hacer una tupla unitaria (un solo elemento)
tupla_unitaria = ("Comida",) #Colocar una coma luego del elemento

#9 - Nota:Se puede crear una tupla sin usar los parentesis (no es tan recomendable) / EMPAQUETADO DE TUPLA
tupla_sinparentesis = 3, 3, 67, 2
print(tupla_sinparentesis)

#10 - DESEMPAQUETADO DE TUPLA / Asignar elementos de tupla a diferentes variables
tupla_empaquetada = ("Hermes", 4, 12, 2001)
nombre, dia, mes, agno = tupla_empaquetada
print(nombre)
print(dia)
print(mes)
print(agno)