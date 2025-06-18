#EJERCICIO1
# def multiplicar_valor(n, m):

#     r = 20
#     if n % 2 == 0:
#         r = n * m
#     else:
#         r = m * n
#     return r

 

# def sumar_valor(x_ref, t_ref, z_ref):

#     x = x_ref[0]
#     x = multiplicar_valor(x, 2)
#     t = multiplicar_valor(x, multiplicar_valor(x, 3))
#     z = multiplicar_valor(x, t)

#     # Actualizar los valores referenciados
#     x_ref[0] = x
#     t_ref[0] = t
#     z_ref[0] = z

 

# # Programa principal (equivalente a "Algoritmo Ejercicio")
# a = [3]
# b = [7]
# c = [4]


# sumar_valor(a, b, c)
# print(a[0], ",", b[0], ",", c[0])

#EJERCICIO2
# def b(div_count):

#     if div_count <= 2:
#         return True
#     else:
#         return False


# def a(num):

#     r = False
#     div_count = 0
#     for c in range(1, num + 1):
#         if num % c == 0:
#             div_count += 1
#             r = b(div_count)
#     return r



# # Programa principal
# for num in range(1, 11):
#     if a(num):
#         print(num, end=" ")

#EJERCICIO3
# def s(l, n):

#     if n == 0:

#         return 0

#     else:

#         return l[n - 1] + s(l, n)  

 

# # Programa principal

# l = [0] * 100

# l[0] = 1

# l[1] = 1

# l[2] = 1

# l[3] = 2

# l[4] = 1

# n = 5

# print(s(l, n))

#EJERCICIO4
# a = int(input("Ingrese el valor: "))

# r = (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0)

# print(r)

#EJERCICIO5
# ct = 1
# t = 0
# s = True

# c = int(input("Ingrese un valor N°1: "))

# while s != False:
#     p = int(input("Ingrese un valor N°2: "))
#     t = t + p
#     ct = ct + 1

#     while ct <= c:
#         print(t, end=",")
#         s = False
#         if ct == c:
#             s = True

#EJERCICIO6
# def c(f):

#     r = f
#     l = len(f)

#     for i in range(0, l, 5):
#         r = f[i:l]
#     return r

# # Programa principal
# f = "HolaMundoCruel"
# print(c(f))

#EJERCICIO7
#d1= 5;  d2= 0  y  d3=25 ?

# Definir variables
# d1 = int(input("Introduce el valor N°1 (día): "))
# d2 = int(input("Introduce el valor N°2 (mes): "))
# d3 = int(input("Introduce el valor N°3 (año): "))

# dd = 100  # valor inicial inválido

# # Determinar los días del mes
# if d2 in [1, 3, 5, 7, 8, 10, 12]:
#     dd = 31
# elif d2 in [4, 6, 9, 11]:
#     dd = 30
# elif d2 == 2:
#     if (d3 % 4 == 0 and not (d3 % 100 == 0)) or (d3 % 400 == 0):
#         dd = 29
#     else:
#         dd = 28
# else:
#     print("A")  

# if d1 < 0 or d1 > dd:
#     print("B")  
# else:
#     if d2 < 0 or d2 > 12:
#         print("C")  
#     else:
#         print("D")  

#EJERCICIO8
# f c(vc, vs):

#     m = vc[0]
#     for i in range(0, vs - 2):  # (vs - 3) en PSeInt equivale a (vs - 2) en Python porque el rango es excluyente
#         if vc[i] > m:
#             m = vc[i]
#     return m

# # Programa principal

# vs = 3
# vc = [0] * vs
# vc[0] = 4
# vc[1] = 6
# vc[2] = 1

# print(c(vc, vs))

#EJERCICIO9
# def s(i_ref, j_val):

#     i_ref[0] = i_ref[0] + 10  # Simula paso por referencia
#     j_val = j_val + 10        # j es por valor
#     print(f" i = {i_ref[0]} / j = {j_val}", end="")

# # Programa principal

# i = [2]  # Usamos una lista para simular referencia
# j = 3
# s(i, j)

# print(f"\ni = {i[0]} / j = {j}")

#EJERCICIO10
# def s(v, t):

#     c = 1
#     if t == 1:
#         c = v[3] + c
#     else:
#         c = s(v, t - 2)
#     return c

# # Programa principal

# print("Ingresar valor:")
# N = int(input())
# v = [0] * N  # Inicializa el vector con N elementos

# for i in range(2, N):
#     v[i] = i * 4
# r = s(v, N)

# print(r)

#EJERCICIO12
# def b(d):

#     if d <= 2:
#         return True
#     else:
#         return False

# def a(num):

#     r = False
#     d = 0
#     for c in range(1, num + 1):
#         if num % c == 0:
#             d += 1
#             r = b(d)
#     return r



# # Programa principal

# for num in range(1, 12):
#     if a(num):
#         print(num, end=" ")

#EJERCICIO11
# Programa principal

# print("Introduce el valor N°1:")

# d1 = int(input())

 

# print("Introduce el valor N°2:")

# d2 = int(input())

 

# print("Introduce el valor N°3:")

# d3 = int(input())

 

# dd = 0

 

# # Determinación de la cantidad de días según el mes

# if d2 in [1, 3, 5, 7, 8, 10, 12]:

#     dd = 31

# elif d2 in [4, 6, 9, 11]:

#     dd = 30

# elif d2 == 2:

#     if (d3 % 4 == 0 and d3 % 100 != 0) or (d3 % 400 == 0):

#         dd = 29

#     else:

#         dd = 28

# else:

#     print("A")

 

# # Validaciones de día y mes

# if (d1 < 0) or (d1 > dd):

#     print("B")

# else:

#     if (d2 < 0) or (d2 > dd):

#         print("C")

#     else:

#         print("D")

def funcion_m(num1, num2):
    resultado = 1200
    if num1 % 2 == 0:
        resultado = 
 
    else:
        resultado = num2 * num1
    return resultado

def funcion_s(x, t, z):
    x = funcion_m(x, 2)
    t = funcion_m(x, funcion_m(x, Respuesta 2 Pregunta 1
 
))
    z = funcion_m(Respuesta 3 Pregunta 1
 
, t)
    return x, t, z

a = 3
b = 7
c = 4

a, b, c = funcion_s(a, b, c)
print(f"{a}, {b}, {c}")