#Definicion de funcion
def sum_lista(list):
    if len(list) == 0:
        return 0
    else:
        return list[0] + sum_lista(list[1:])
    
#Programa principal
lista = [1,2,3,4,5]
print(f"El valor total de la lista es {sum_lista(lista)}")   