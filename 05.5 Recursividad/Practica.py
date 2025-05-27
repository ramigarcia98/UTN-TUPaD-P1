import sys
sys.setrecursionlimit(20000) #Aumenta el limite de recursiones

#Definicio de funcion

def factorial(x): #Opcion sin recursividad
    f = 1
    for i in range(1, x + 1):
        f *= i
    return f

def factorial_recursividad(x):
    return 1 if x == 0 else x * factorial_recursividad(x - 1) #Opcion corta "mejor"
#    if x == 0:  #Opcion "larga"
#        return 1
#    else:
#        return x * factorial_recursividad(x - 1)

#Programa principal
print(factorial_recursividad(5))
#Para un numero muy grande da un error porque excesede las 1000 llamadas
