#Ejercicio 1
#1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range.

# lista=list(range(4,101,4))
# print(lista)

#Ejercicio2
#Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el penúltimo. 
#¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el indexing con números negativos!

# import random

# lista=[0]*5

# for i in range(5):
#     lista[i] = random.randint(0, 1000)

# print(lista)
# print(lista[3])

#Ejercicio3
#Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por pantalla. 
#Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior. Por ejemplo:

# lista=[]
# for i in range(3):
#     print(f"Escriba el elemento que desee en la posicion {i}")
#     lista.append(input())
# print(lista)

#Ejercicio4
#Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, respectivamente.
#Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra en los videos o bien investigar 
#cómo funciona el indexing con números negativos! animales = ["perro", "gato", "conejo", "pez"]

# animales = ["perro", "gato", "conejo", "pez"]
# print(animales)

# animales[1] = "loro"
# animales[-1] = "oso"
# print(animales)

#Ejercicio5
#Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.

# numeros = [8,15,3,22,7]
# numeros.remove(max(numeros))
# print(numeros)
# print("El programa identifica el valor MAXIMO de la lista mediante max() y lo elimina de la misma")

#Ejercicio6
#Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por pantalla 
#los dos primeros.

# import random

# lista=list(range(10,31,5))
# print(lista)
# print(lista[0:2])

#Ejercicio7
#Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores cualesquiera.
#autos = ["sedan", "polo", "suran", "gol"]

# autos = ["sedan", "polo", "suran", "gol"]
# print(autos)

# print("Ingrese otro modelo de auto para la posicion 1")
# autos[1] = input()
# print("Ingrese otro modelo de auto para la posicion 2")
# autos[2] = input()

# print(autos)

#Ejercicio8
#Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append directamente. 
#Imprimir la lista resultante por pantalla.

# doble=[]
# print(doble)

# doble.append(5*2)
# doble.append(10*2)
# doble.append(15*2)

# print(doble)

#Ejercicio9
#Dada la lista “compras”, cuyos elementos representan los productos comprados por diferentes clientes:
#compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
#a) Agregar "jugo" a la lista del tercer cliente usando append.
#b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
#c) Eliminar "pan" de la lista del primer cliente.
#d) Imprimir la lista resultante por pantalla

# compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
# print(compras)

# print("A)")
# compras[2].append("jugo")
# print(compras)

# print("B)")
# compras[2][1] = "tallarines"
# print(compras)

# print("C)")
# compras[0].remove("pan")
# print(compras)

# print("D)")
# print(compras)

#Ejercicio10
#Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
#● Posición lista_anidada[0]: 15
#● Posición lista_anidada[1]: True
#● Posición lista_anidada[2][0]: 25.5
#● Posición lista_anidada[2][1]: 57.9
#● Posición lista_anidada[2][2]: 30.6
#● Posición lista_anidada[3]: False
#Imprimir la lista resultante por pantalla.

lista_anidada = [15,True, [25.5,57.9,30.6],False]
print(lista_anidada)