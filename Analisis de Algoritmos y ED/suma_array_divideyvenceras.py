def suma_array(lista):
    if len(lista)==1:
        return lista[0] #caso base: solo queda un elemento en la lista
    else:
        return lista[0] + suma_array(lista[1:]) #suma el actual primer elemento en la lista con la siguiente llamada recursiva
    
print(suma_array([30,15,5]))

def suma_array_libro(lista2):
    if lista2==[]:
        return 0 #caso base: no hay mas elementos en la lista
    else:
        return lista2[0] + suma_array_libro(lista2[1:]) #suma el primer elemento de la actual lista con la siguiente llamada recursiva
    
print(suma_array_libro([30,15,15]))