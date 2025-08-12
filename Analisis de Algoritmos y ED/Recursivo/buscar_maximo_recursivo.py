def maximo_lista(lista):
    if len(lista)==1:
        return lista[0]
    else:
        resto_max = maximo_lista(lista[1:])
        return lista[0] if lista[0]>resto_max else resto_max
    
print(maximo_lista([203,3,54,22,101,99,5,2,400]))