def quick_sort(array):
    if len(array)<2:
        return array
    else:
        pivote = array[0]
        menores = [elemento for elemento in array[1:] if elemento <= pivote] #array o lista por comprension, anade a la lista solo lo menor al pivote
        mayores = [elemento for elemento in array[1:] if elemento > pivote] #array o lista por comprension, anade a la lista solo lo mayor al pivote
        
        return quick_sort(menores) + [pivote] + quick_sort(mayores)
    
    

lista = [6, 2, 4, 9, 10, 11, 8, 1]
print(quick_sort(lista))