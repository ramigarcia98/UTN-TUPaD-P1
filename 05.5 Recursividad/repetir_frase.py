#Definicio de funcion

def repetir_frase(num, mensaje):
    if num>=1:
        print(mensaje)
        repetir_frase(num-1,mensaje)

#Programa principal

num = int(input("Ingrese la cantidad de veces que desea repetir una frase: "))
mensaje = input("Ingrese la frase a repetir: ")
repetir_frase(num, mensaje)
