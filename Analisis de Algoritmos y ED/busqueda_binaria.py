def binary_search(list, item):
    low = 0
    high = len(list) - 1
    
    while low <= high:
        mid = (low + high) // 2 #Division entera (redondeo hacia abajo)
        guess = list[mid] #Adivinar
        
        if guess==item:
            return mid
        if guess>item:
            high = mid - 1
        else:
            low = mid + 1
    return None

my_list = [1,15,45,67,89,100]

print(binary_search(my_list, 45)) #Devuelve posicion de numero que si esta en la lista
print(binary_search(my_list, 24)) #Devuelve None para numero que no esta en la lista
