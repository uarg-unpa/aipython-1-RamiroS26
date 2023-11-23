#1
lista = []

#2
lista_7 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#3
print(len(lista_7))

#4
frutas_favoritas = ['durazno', 'cereza', 'uva', 'naranja']

#a
print(len(frutas_favoritas))

#b
frutas_favoritas.pop(0)

#c
frutas_favoritas.append('pera')

#d
print(frutas_favoritas)

#5
lista = [10, 20, 30, 40, 50]
print(lista[0], lista[len(lista)//2], lista[-1])

#6
datos = ['Ramiro', 29, 1.80, 'Soltero', 'Jujuy']

#7
companias = ['Google', 'Tesla', 'Microsoft']

#8
for dato in datos:
    print(dato)

#9
for indice, compania in enumerate(companias):
    print(f'Índice: {indice}, Compañía: {compania}')

#10
companias[0] = 'Amazon'
print(companias)

#11
numeros = list(range(1, 11))

#a
print(numeros[:3])

#12
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

#a
print(letras[::2])

#13
lista = [26, 'Hola mundo', 3.1415, True, None]

#a
print(lista[::-1])

#14
palabras = ['no', 'tengo', 'palabras', 'favoritas']

#a
sub_palabras = palabras[1:4]

#15
flores = ['rosas', 'orquídea', 'lirio', 'tulipan', 'margarita', 'dalia', 'hortensia']

#a
print(flores[2:5])

#b
print(flores[1::2])

#c
print(flores[::3])