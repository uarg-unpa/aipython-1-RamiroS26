#1
def multiplicacion(a, b):
    return a * b

#2
def multiplicacion(a=1, b=1):
    return a * b

#3
def mensaje(nombre):
    return f'Hola {nombre}, tuki'

#4
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f'{numero} x {i} = {numero * i}')

#5
def es_par(numero):
    if numero % 2 == 0:
        return 'Par'
    else:
        return 'Impar'

#6
def factorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * factorial(numero - 1)

#7
def maximo(a, b, c):
    return max(a, b, c)

#8
def invertir_string(texto):
    return texto[::-1]

#9
def multiplicar(lista):
    resultado = 1
    for numero in lista:
        resultado *= numero
    return resultado

#10
def es_palindromo(cadena):
    cadena = cadena.lower()
    return cadena == cadena[::-1]

#11
def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

#12
def vocales(lista):
    vocales = "aeiouAEIOU"
    return sum(1 for char in lista if char in vocales)

#13
def intercalar_listas(lista1, lista2):
    return [elemento for tuple in zip(lista1, lista2) for elemento in tuple]

#14
def promedio_lista(lista):
    if not lista:
        return 0
    return sum(lista) / len(lista)