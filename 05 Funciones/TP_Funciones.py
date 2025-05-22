
import funciones_creadas

#Ejercicio1
# funciones_creadas.imprimir_mensaje()

#Ejercicio2
# nombre_usuario = input("Por favor, ingresa tu nombre: ")
# saludo = funciones_creadas.saludar_usuario(nombre_usuario)

#Ejercicio3
# nombre= input("Por favor, ingresa tu Nombre: ")
# apellido=input("Por favor, ingresa tu Apellido: ")
# edad=input("Por favor, ingresa tu edad: ")
# residencia=input("Por ultimo, ingresa tu direccion: ")
# presentacion = funciones_creadas.informacion_personal(nombre, apellido, edad, residencia)

#Ejercicio4
# radio = funciones_creadas.leer_numero_valido("Ingrese el radio",1)
# area = funciones_creadas.area_circulo(radio)
# perimetro = funciones_creadas.perimetro_circulo(radio)


#Ejercicio5
# segundos = funciones_creadas.leer_entero_validad("Ingrese los segundo para convertir en horas",1)
# hora = funciones_creadas.segundos_a_hora(segundos)

#Ejercicio6
# numero = funciones_creadas.leer_entero_validad("Ingrese el numero del que desea saber su tabla de multiplicar",1)
# tabla = funciones_creadas.tabla_multiplicar(numero)

#Ejercicio7
# a = float(input("Ingrese un numero: "))
# b = float(input("Ingrese otro numero: "))
# tabla = funciones_creadas.operaciones_basicas(a, b)

# print(f"{a} + {b} = {tabla[0]}")
# print(f"{a} - {b} = {tabla[1]}")
# print(f"{a} * {b} = {tabla[2]}")
# print(f"{a} / {b} = {tabla[3]}")

#Ejercicio8
# peso = float(input("Ingrese su peso en Kg: "))
# altura = float(input("Ingrese su altura en mts: "))
# imc = funciones_creadas.calcular_imc(peso,altura)
# print(f"Su IMC es: {imc}")

#Ejercicio10
# a = float(input("Ingrese N1: "))
# b = float(input("Ingrese N2: "))
# c = float(input("Ingrese N3: "))
# promedio = funciones_creadas.calcular_promedio(a, b, c)
# print(f"El promedio entre {a}, {b} y {c} es: {promedio}")

#Ejercicio9
celcius = float(input("Ingrese el grado Celsius que quiere pasar a Fahrenheit: "))
fahrenheit = funciones_creadas.celsius_a_fahrenheit(celcius)
print(f"{celcius}°C son {fahrenheit}°F")