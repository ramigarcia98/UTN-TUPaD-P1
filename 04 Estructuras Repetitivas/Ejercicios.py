#Ejercicio 1

# for i in range(0,101,1):
#     print(i)

#Ejercicio 2

# num=int(input("Ingrese un numero:"))
# digito=0
# cont=0

# if num==0:
#     digito=1

# elif digito==0:
#     while num>0:
#         num = num//10
#         cont = cont+1

# print("El numero ingresado tiene",cont,"digitos")

#Ejercicio 3

# num1=int(input("Ingrese el primer numero: "))
# num2=int(input("Ingrese el seguno numero: "))
# sum=0

# for i in range(num1+1,num2,1):
#     print(i)
#     sum=sum+i

# print("La suma de todos los numero ingresados es:",sum)

#Ejercicio 4

# print("Numero 1")
# num=int(input())
# sum=0
# i=1

# while num!=0:
#     i=i+1
#     sum=sum+num
#     print("Numero ",i)
#     num=int(input())

# print("La suma de los numeros ingresados es:",sum)

#Ejercicio 5

# from random import randrange
# num_aleatorio=randrange(9)

# print("ADIVINA EL NUMERO ENTRE 0 Y 9")
# num=int(input("Ingrese un numero : "))
# cont=1

# while num!=num_aleatorio:
#     cont=cont+1
#     num=int(input("Ingrese nuevamente otro numero: "))

# print("En",cont,"intentos se adivino el numero")

#Ejercicio 6

# for i in range (100,0,-1):
#     if i%2==0:
#         print(i)


#Ejercicio 7

# num=int(input("SUMAR LOS NUMEROS ENTRE O Y "))
# sum=0

# for i in range (0,num+1):
#     sum=sum+i

# print("La suma de los numeros comprendidos ente 0 y ",num,"es:",sum)

#Ejercicio 8

# pos=0
# neg=0
# par=0
# impar=0

# for i in range(1,5+1):
#     print("N°",i)
#     num=int(input())

#     if num%2==0 and num>0:
#         par=par+1
#         pos=pos+1
#     elif num%2==0 and num<0:
#         par=par+1
#         neg=neg+1
#     elif num%2!=0 and num>0:
#         impar=impar+1
#         pos=pos+1
#     elif num%2!=0 and num<0:
#         impar=impar+1
#         neg=neg+1

# print("La cantidad de numeros pares es:",par)
# print("La cantidad de numeros impares es:",impar)
# print("La cantidad de numeros positivos es:",pos)
# print("La cantidad de numeros negativos es:",neg)

#Ejercicio 9

# sum=0

# for i in range(1,5+1):
#     print("N°",i)
#     num=int(input())
#     sum=sum+num

# print(f"El promedio de los numeros sumados es:{sum/i}")

#Ejercicio 10

# num=int(input("Ingrese un numero:"))
# invertido=0

# while num>0:
#     digito=num%10 #de esta manera obtengo el ultimo digito
#     invertido=invertido*10+digito #agrego el digito al numero invertido
#     num=num//10 #elimina el ultimo digito
# print("El numero invertido es:",invertido)
