def contar_elementos(lista):
    if lista==[]:
        return 0 #caso base: no hay elementos
    else:
        return 1 + contar_elementos(lista[1:]) #suma 1 elemento y le suma la siguiente llamada recursiva
    
print(contar_elementos([1,2,3,4,5,6,7,8,9,10,11,12]))