# Ejercicio 3: 
# • Crea un programa que evalúe si una dirección de correo electrónico es válida o no en 
# función de si tiene “@” o “.” Hay que tener en cuenta que la dirección se considera 
# correcta si solo tiene una “@” y si tiene uno o más “.” 

correo_electronico = input("Ingrese el nuevo correo: ")
contador_arroba=0
contador_puntos=0

for caracter in correo_electronico:
    if caracter=="@":
        contador_arroba += 1

    if caracter==".":
        contador_puntos +=1

if contador_arroba==1 and contador_puntos>0:
    print("Correo valido")
else:
    print("Correo invalido")