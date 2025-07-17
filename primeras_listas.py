#Primera lista
mi_lista=["Flori", "Josue", "Fabi", "Josue"]

#Devolver elementos de la listade
print(mi_lista[:]) #Sintaxis para imprimir la lista completa

print(mi_lista[2]) #Sintaxis para imprimir el elemento de un indice especifico

print(mi_lista[-3]) #Devolver elemento del indice del final hacia el inicio de la lista (inicia desde 1)

print(mi_lista[1:3]) #Devuelve porcion de la lista, incluye el indice inicial pero el final no

print(mi_lista[:2]) #Devuelve desde el inicio hasta uno antes del indicado

print(mi_lista[1:]) #Devuelve desde el indice indicado hasta el final de la lista

#Agregar elementos a una lista
mi_lista.append("Maria") #Agrega elemento al final de la lista
mi_lista.insert(0, "Brayan") #Parametros (indice, elemento) / Inserta elemento en indice concreto
mi_lista.extend(["Emilce", "Dilan", "Mauricio"]) #Anade varios elementos al final de la lista

#Devuelve el indice donde se encuentra el elemento dado
print(mi_lista.index("Dilan")) 

#Verificar si un elemento pertenece o esta en una lista (Boolean)
print("Brayan" in mi_lista)

#Eliminar elementos de la lista
mi_lista.remove("Josue") #Elimina un elemento especifico de la lista, el primero que encuentre
mi_lista.pop() #Elimina el ultimo elemento de la lista

print(mi_lista[:])


#Unir dos lista diferentes
mi_lista2 = [2, 3, 4, 5]
listas_unidas = mi_lista + mi_lista2 #Operador de suma

print(listas_unidas[:]) 

#Repetidor (hacer una lista repitiendo una serie de elementos)  

lista_repeticion = [1, 2, 3, 4, 5] * 4 #Operador de resta
print(lista_repeticion[:]) 