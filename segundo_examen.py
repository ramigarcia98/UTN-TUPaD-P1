# def funcion_m(num1, num2):
#     resultado = 1200
#     if num1 % 2 == 0:
#         resultado = num1 * num2
#     else:
#         resultado = num2 * num1
#     return resultado

# def funcion_s(x, t, z):
#     x = funcion_m(x, 2)
#     t = funcion_m(x, funcion_m(x,3))
#     z = funcion_m(x, t)
#     return x, t, z

# a = 3
# b = 7
# c = 4

# a, b, c = funcion_s(a, b, c)
# print(f"{a}, {b}, {c}")

# def funcion_s(num1, num2):

#     num1 = num1 + 10

#     num2 = num2 + 10

#     print(f" i = {num1} / j = {num2}", end="")



# num1 = 2

# num2 = 3

# funcion_s(num1, num2)

# print(f"\ni = {num1} / j = {num2}")

# anio = int(input("Ingrese el valor: "))

 

# es_bisiesto = (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

 

# print(not es_bisiesto )

# def funcion_c(frase):

#     resultado = frase

#     longitud = len(frase)

#     for i in range(0, longitud, 5):
#         resultado =frase[i:longitud]

#     return resultado



# frase = "HolaMundoCruel"

# print(funcion_c(frase))

# def funcion_c(vector,tamanio_vector):
#     max = vector[0]

#     for i in range(0,tamanio_vector): 
#         if vector[i] >max:

#             max = vector[i]

#     return max

 

# tamanio_vector = 3

# vector = [0] * tamanio_vector  

# vector[0] = 4

# vector[1] = 6

# vector[2] = 1

 

# print(funcion_c(vector, tamanio_vector))





# def funcion_b(contador):

#     if contador <= 2:

#         return True

#     else:

#         return False



# def funcion_a(numero):

#     contador = 0

#     for candidato in range(1, numero + 1):

#         if numero % candidato == 0:

#             contador += 1

#             if not funcion_b(contador+1):

#                 return False

#     return True



# for numero in range(1, 11):

#     if funcion_a(numero):

#         print(numero, end=" ")


# def funcion_s(vector, posicion):

#     total = 1

#     if posicion == 1:

#         total = vector[1] + total

#     else:

#         total = funcion_s(vector, posicion - 2)

   

#     return total



# vector_a = []

# num1 = int(input("Ingresar valor: "))



# vector_a = [0] * (num1 + 1)

# for i in range(1, num1):

#     vector_a[i] = i * 2

# resultado = funcion_s(vector_a, num1)

# print(resultado)



# i = 1

# while i<=2:

#     print(f"Iteración exterior: {i}", end=" ")

#     j = 1

#     while j <2:  

#         print(f"Iteración interior: {j}", end=" ")

#         j += 1

#     i += 1

# def ejercicio():
#     dia = int(input("Introduce el valor N°1: "))
#     mes = int(input("Introduce el valor N°2: "))
#     anio = int(input("Introduce el valor N°3: "))

#     if mes in [1, 3, 5, 7, 8, 10, 12]:
#         ultimo_dia_mes = 31
#     elif mes in [4, 6, 9, 11]:
#         ultimo_dia_mes = 30
#     elif mes == 2:
#         if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
#             ultimo_dia_mes = 29
#         else:
#             ultimo_dia_mes = 28
#     else:
#         ultimo_dia_mes = 0

#     if  not (dia < 0 and dia < ultimo_dia_mes):
#         print("B")
#     else:
#         if mes < 0 or mes > 12:
#             print("C")
#         else:
#             print("D")

# ejercicio()

# for t in range(1,3):  

#     for n in range(1,4): 

#         print(t * n, end="")

# contador = 1

# t = 0

# bandera = True



# num1 = int(input("Ingrese un valor N°1: "))



# while bandera == True:

#     while contador <= num1:

#         num2 = int(input("Ingrese un valor N°2: "))

#         t = t + num2

#         print(t, end=",")

#         contador =contador+1

#         if contador > num1:

#             bandera = False

#         else:

#             bandera = True

def funcion_s(vector, largo):
    total = 0
    if largo == 0:
        total = 0
    else:
        total = vector[largo - 1] + funcion_s(vector, largo - 1) 
    return total

vector = [0] * 100
vector[0] = 1
vector[1] = 1
vector[2] = 1
vector[3] = 2
vector[4] = 1
largo = 6

print(funcion_s(vector,largo -2))