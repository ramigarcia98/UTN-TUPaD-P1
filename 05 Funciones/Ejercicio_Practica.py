# Desarrollar un algoritmo de forma modularizada que permita
# ingresar un numero natural. La computadora debera mostrar
# si el numero es o no primo 

# Definicion de funciones
def leer_entero_validad(mensaje, min=float("-Inf"), max=float("+Inf")): #El segundo y tercer argumento, es para el caso en el que no sea desee poner rangos de numero, el numero por defaul que te ingrese sea entre -inf y +inf
    n = int(input(f"{mensaje}: "))
    while n<min or n>max:
        n = int(input(f"ERROR. {mensaje}: "))
    return n 

def obtener_resto(num1, num2):
    return num1-num2*(num1//num2)

def es_multiplo(x, y):
    return obtener_resto(x, y)==0

def es_primo(numero):
    cont = 2 
    mitad = numero//2
    while cont<=mitad and not es_multiplo(numero,cont):
        cont += 1
    return cont>mitad

def informar_si_numero_es_primo(numero):
    if es_primo(numero):
        print(f"El numero {numero} es primo")
    else:
        print(f"El numero {numero} NO es primo ") 



# Programa principal

num = leer_entero_validad("Ingresa un numero natural",1)
informar_si_numero_es_primo(num)