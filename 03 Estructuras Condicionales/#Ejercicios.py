# #Ejercicio 1

# edad= int(input("Ingrese su edad: "))

# if edad >= 18:
#     print("Es mayor de edad")
# else:
#     print("Es menor de edad")

#Ejercicio 2

# nota=int(input("Ingrese su nota: "))

# if nota >= 6:
#     print("APROBADO")
# else:
#     print("DESAPROBADO")

#Ejercicio 3

# num=int(input("Ingrese un numero: "))

# if num % 2 == 0:
#     print("Ha ingresado un numero par")
# else:
#     print("Por favor, ingrese un numero par")

#Ejercicio 4

# edad=int(input("Ingrese su edad: "))

# if edad < 12:
#     print("Calificado como NIÑO/A")
# elif 12 <= edad < 18:
#     print("Calificado como Adolescente")
# elif 18 <= edad < 30:
#     print("Calificado como ADULTO/A JOVEN")
# else:
#     print("Calificado como ADULTO/A")

#Ejercicio 5

# clave=input("Ingrese una contraseña que tenga entre 8 y 14 caracteres: ")

# if 8 <= len(clave) <= 14:
#     print("Ha ingresado una contraseña correcta")
# else:
#     print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#Ejercicio 6

# from statistics import mode, median, mean
# from random import randint

# numeros_aleatorios = [randint(1, 100) for i in range(50)]

# print(f"Media: {mean(numeros_aleatorios)}")
# print(f"Mediana: {median(numeros_aleatorios)}")
# print(f"Moda: {mode(numeros_aleatorios)}")

# if mean(numeros_aleatorios) > median(numeros_aleatorios) and median(numeros_aleatorios) > mode(numeros_aleatorios):
#     print("Sesgo positivo")
# elif mean(numeros_aleatorios) < median(numeros_aleatorios) and median(numeros_aleatorios) < mode(numeros_aleatorios):
#     print("Sesgo negativo")
# elif mean(numeros_aleatorios) == median(numeros_aleatorios) ==  mode(numeros_aleatorios):
#     print("Sin sesgo")

#Ejercicio 7

# frase=input("Ingrese un frase o una palabra: ")

# if frase[-1].lower() == "a" or frase[-1].lower() == "e" or frase[-1].lower() == "i" or frase[-1].lower() == "o" or frase[-1].lower() == "u":
#     print(f"{frase}!")
# else:
#     print(frase)

#Ejercicio 8

# nombre=input("Ingrese su nombre: ")

# print("Si quiere su nombre en mayúsculas presione (1)")
# print("Si quiere su nombre en minuscula presione (2)")
# print("Si quiere su nombre con la primera letra mayúscula presione (3)")

# opcion=int(input("OPCION: "))

# if opcion == 1:
#     print(nombre.upper())
# elif opcion == 2:
#     print(nombre.lower())
# elif opcion == 3:
#     print(nombre.title())
# else:
#     print("No se selecciono una opcion valida")

#Ejercicio 9
 
# terremoto=float(input("Ingrese la magnitud del terremoto: "))

# if terremoto <= 3:
#     print("La magnitud del terremoto ingresada corrsponde a un terremoto MUY LEVE")
# elif 3 <= terremoto < 4:
#     print("La magnitud del terremoto ingresada corrsponde a un terremoto LEVE")
# elif 4 <= terremoto < 5:
#     print("La magnitud del terremoto ingresada corrsponde a un terremoto MODERADO")
# elif 5 <= terremoto < 6:
#     print("La magnitud del terremoto ingresada corrsponde a un terremoto FUERTE")
# elif 6 <= terremoto < 7:
#     print("La magnitud del terremoto ingresada corrsponde a un terremoto MUY FUERTE")
# else:
#     print("La magnitud del terremoto ingresada corrsponde a un terremoto EXTREMO")

#Ejercicio 10

print("Ingrese el emisferio, mes y dia en el que se encuentra")
emisferio=input("Emisferio (N/S): ")
mes=int(input("Mes (numero): "))
dia=int(input("Dia:"))

if emisferio.upper() == "N":
    if (mes == 12 and dia >= 21) or (mes <=3 and dia <= 20):
        print("Usted se encuentra en INVIERNO")
    elif (mes >= 3 and dia >= 21) or (mes <= 6 and dia <= 20):
        print("Usted se encuentra en PRIMAVERA")
    elif (mes >= 6 and dia >= 21) or (mes <= 9 and dia <= 20):
        print("Usted se ecnuentra en VERANO")
    else:
        print("Usted se encuentra en OTOÑO")

elif emisferio.upper() == "S":
    if (mes == 12 and dia >= 21) or (mes <=3 and dia <= 20):
        print("Usted se encuentra en VERANO")
    elif (mes >= 3 and dia >= 21) or (mes <= 6 and dia <= 20):
        print("Usted se encuentra en OTOÑO")
    elif (mes >= 6 and dia >= 21) or (mes <= 9 and dia <= 20):
        print("Usted se ecnuentra en INVIERNO")
    else:
        print("Usted se encuentra en PRIMAVERA")