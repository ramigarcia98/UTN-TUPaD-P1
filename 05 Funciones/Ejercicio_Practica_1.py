# Desarrollar un algoritmo de forma modularizada que permita
# ingresar un numero natural. La computadora debera
# demostrar si el numero es o no perfecto.


# Definicion de funciones

def leer_entero_validad(mensaje, min=float("-Inf"), max=float("+Inf")): #El segundo y tercer argumento, es para el caso en el que no sea desee poner rangos de numero, el numero por defaul que te ingrese sea entre -inf y +inf
    n = int(input(f"{mensaje}: "))
    while n<min or n>max:
        n = int(input(f"ERROR. {mensaje}: "))
    return n 


def informar_si_numero_es_perfecto(numero):
    if es_perfecto(numero):
        print(f"El numero {numero} es perfecto")
    else:
        print(f"El numero {numero} NO es perfecto")


def es_perfecto(numero):
    return sumatoria_divisores_propios(numero)==numero


def sumatoria_divisores_propios(numero):
    sumatoria=0
    for i in range (1,(numero//2)+1):
        if es_multiplo(numero,i):
            sumatoria += i
    return sumatoria


def es_multiplo(x, y):
    return obtener_resto(x, y)==0


def obtener_resto(num1, num2):
    return num1-num2*(num1//num2)


# Programa principal
num = leer_entero_validad("Ingresa un numero natural",1)
informar_si_numero_es_perfecto(num)