#Definicion de funcion 

def suma_recursiva(num):
    if num == 0:
        return 0
    else:
        return num + suma_recursiva(num-1)

#Programa principla

num = int(input("Ingrese un numero hasta el cual desee sumar: "))
print(f"La suma desde 1 hasta {num} es: ",suma_recursiva(num))