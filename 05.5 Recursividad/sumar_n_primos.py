'''
Realizar una funcion recursiva que permita sumar los n valores primos

Propiedad matematica:
Un numero no primo tiene al menos un divisor diferente de 1 y de si mismo.
Si un numero n tiene un divisor d tal que d<=sqrt{n}, entonces
n puede expresarse como n=d.k, donde k>=sqrt{n}.
Por ejemplo:
Para n=36, los divisores son 2,3,4,6,9,12,18 y basta
comprobar hasta 36=sqrt{36}=6
Esto significa que si no encontramos divisor de n menores
o iguales a sqrt{n}, entonces n es primo.

'''
def es_primo(numero):
    if numero <= 1:
        return False
    for i in range (2, int(numero**0.5)+1):
        if numero % i == 0:
            return False
    return True

def sum_n_primos(num):
    if num == 1:
        return 0
    elif es_primo(num):
        return num + sum_n_primos(num-1)
    else:
        return sum_n_primos(num-1)

print(sum_n_primos(5))