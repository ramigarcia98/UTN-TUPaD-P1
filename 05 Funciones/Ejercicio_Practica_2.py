# Desarrollar un algoritmo de forma modularizada que permita ingresar un ancho y un alto (ambos positivos)
# La computadora debe dibujar una matriz de "X" en la consola


import funciones_creadas
# Definicion de funciones
def imprimir_matriz(ancho,alto,simbolo="X"):
    for i in range(alto):
        funciones_creadas.imprimir_simbolo(simbolo, ancho)
    


# Programa principal 
ancho = funciones_creadas.leer_entero_validad("Ingrese el ANCHO", 1)
alto = funciones_creadas.leer_entero_validad("Ingrese el ALTO", 1)
imprimir_matriz(ancho,alto,"R")