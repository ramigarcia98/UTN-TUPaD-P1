import math

def leer_entero_validad(mensaje, min=float("-Inf"), max=float("+Inf")): #El segundo y tercer argumento, es para el caso en el que no sea desee poner rangos de numero, el numero por defaul que te ingrese sea entre -inf y +inf
    n = int(input(f"{mensaje}: "))
    while n<min or n>max:
        n = int(input(f"ERROR. {mensaje}: "))
    return n

def leer_numero_valido(mensaje, min=float("-Inf"), max=float("+Inf")): 
    n = float(input(f"{mensaje}: "))
    while n<min or n>max:
        n = float(input(f"ERROR. {mensaje}: "))
    return n

def imprimir_simbolo(simbolo, veces):
    print(sucesion_simbolos(simbolo, veces))

def sucesion_simbolos(simbolo, veces):
    sucesion=""
    for i in range(veces):
        sucesion += simbolo
    return sucesion 

def imprimir_matriz(ancho,alto,simbolo="X"):
    for i in range(alto):
        imprimir_simbolo(simbolo, ancho)

def imprimir_mensaje(mensaje="Hola Mundo!"):
    print(mensaje)

def saludar_usuario(nombre):
    print(f"Hola {nombre}!")

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy { nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

def area_circulo(radio):
    area = math.pi * radio**2
    print(f"El circulo de radio {radio} tiene un area de {area}")

def perimetro_circulo(radio):
    perimetro = 2 * math.pi * radio
    print(f"El circulo de radio {radio} tiene un perimetro de {perimetro}")

def segundos_a_hora(segundos):
    horas= segundos/3600
    print(f"{segundos} segundos equivalen a {horas} horas")

def tabla_multiplicar(numero):
    for i in range(1,11):
        tabla=numero*i
        print(f"{numero} x {i} = {tabla}")

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    if b != 0:
        division = a / b
    else:
        division = "Indefinida (división por cero)"
    return (suma, resta, multiplicacion, division)

def calcular_imc(peso, altura):
    IMC = round(peso / (altura ** 2),2)
    return IMC

def calcular_promedio(a, b, c):
    suma = a + b + c
    promedio = suma / 3
    return promedio

def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * (9 / 5)) + 32
    return fahrenheit