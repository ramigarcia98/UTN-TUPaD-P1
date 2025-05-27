'''
1) Crea una función recursiva que calcule el factorial de un número. 
Luego, utiliza esa función para calcular y mostrar en pantalla el 
factorial de todos los números enteros entre 1 y el número que indique el usuario
'''

# def factorial_recursivo(num):
#     return 1 if num == 0 else num * factorial_recursivo(num-1)
#     '''
#     if num == 1:
#         return 1
#     else:
#         return num * factorial_recursivo(num-1)
#     '''

# num = int(input("Ingrese el numero del cual desea saber su factorial: "))
# print (factorial_recursivo(num))

'''
2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada.
 Posteriormente, muestra la serie completa hasta la posición que el usuario especifique.
Serie de Fibonacc: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1.597, 2.584, 4.181, 6.765,
 10.946, 17.711, 28.657, 46.368, …
 '''

# def fibonacci_recursivo(posicion):
#     if posicion == 0:
#         return 0 
#     elif posicion == 1:
#         return 1
#     else:
#         return fibonacci_recursivo(posicion-1) + fibonacci_recursivo(posicion - 2)

# posicion = int(input("Ingrese la posicion de la cual desea sabes la serie de Fibonacci: "))
# print(fibonacci_recursivo(posicion))

'''
3) Crea una función recursiva que calcule la potencia de un número base elevado a un exponente,
 utilizando la fórmula 𝑛𝑚= 𝑛∗𝑛(𝑚−1).
 Prueba esta función en un algoritmo general.
'''
# def potencia_recursiva(base, exponente):
#     if exponente == 0:
#         return 1
#     else:
#         return base * potencia_recursiva(base, exponente - 1)

# base = int(input("Ingrese la base de la potencia: "))
# exponente = int(input("Ingrese el exponente: "))
# print(f"{base}^{exponente}={potencia_recursiva(base,exponente)}")

'''
4) Crear una función recursiva en Python que reciba un número entero positivo en base decimal
 y devuelva su representación en binario como una cadena de texto.
'''
# def decimal_a_binario(decimal):
#     if decimal == 0:
#         return "0"
#     else:
#         residuo = decimal % 2
#         return decimal_a_binario(decimal // 2) + str(residuo)
        
    
# decimal = int(input("Ingrese un numero decimal: "))
# print(f"El numero {decimal} en binario es {decimal_a_binario(decimal)}")

'''
5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena de texto
 sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es.
'''
# def es_palindromo(palabra):
#     if len(palabra) <= 1:
#         return True
    
#     if palabra[0] != palabra[-1]:
#         return False

#     return es_palindromo(palabra[1:-1])

# palabra = input("Ingrese una frase sin espacio: ")
# print(es_palindromo(palabra))

'''
6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un número entero
 positivo y devuelva la suma de todos sus dígitos.
'''

# def suma_digitos(n):
#     if n == 0:
#         return 0
#     else:
#         resto = n % 10
#         return resto + suma_digitos(n // 10) 

# n = int(input("Ingrese un numero: "))
# print(f"La suma de los digitos del numero {n} es igual a {suma_digitos(n)}")

'''
7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n bloques,
en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al último nivel con un solo bloque.
Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el nivel más bajo
y devuelva el total de bloques que necesita para construir toda la pirámide.
'''

# def contar_bloques(n):
#     if n == 0:
#         return n
#     else:
#         return n + contar_bloques(n-1)

# n = int(input("Ingrese el numero de bloques de la base: "))
# print(f"Comenzando con esa cantidad de bloques, para hacer una piramide necesitaras {contar_bloques(n)} bloques")

'''
8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un número entero
positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces aparece ese dígito dentro del número.
'''
def contar_digito(n, d):
    
    if n == 0:
        return 0
    if (n % 10) == d:
        contador = 1
    else: 
        contador = 0
    return contador + contar_digito(n // 10, d)
         
n = int(input("Ingrese un numero: "))
d = int(input("Ingrese algun digito del 0 al 9: "))
print(f"El numero {n} tiene {contar_digito(n,d)} veces el digito {d}")