#1

#numero = 0
#while numero <= 100:
#    print(numero)
#    numero += 1

#2

#for num in range (101):
#    print(num, end=' ')

#3

#num = 10
#while num >= 0:
#    print(num, end=' ')
#    num -= 1

#for num in range(10, -1, -1):
#    print(num, end=' ')

#4

#num1 = int(input("Ingrese un numero entero: "))
#num2 = int(input("Ingrese otro numero entero: "))
#for num in range(num1+1,num2):
#    print(num, end=' ')

#5

#for i in range(1,8):
#    print("#"*i)

#6

#for i in range(8):
#    for j in range(8):
#        print("#", end='')
#    print("")

#7

#nombre = input("Ingrese su nombre de usuario: ")
#numero = int(input("Ingrese un numero entero: "))
#for i in range(numero):
#    print(nombre)

#8

#num = int(input("Ingrese un numero mayor a 3: "))
#for i in range(1,num+1,2):
#    print(i)

#9

#for i in range(0,12):
#    print(f"{i} x {i} = {i*i}")

#10

#for i in range(7):
#    for j in range(i, 7):
#        print(f"{i} : {j}")

#11

#num = int(input("Ingrese un numero entero: "))
#for i in range(1, num + 1, 2):
#    for j in range(i, 0, -2):
#        print(j, end=' ')
#    print()

#12

#n = int(input("Ingrese un numero natural: "))
#suma = 0
#suma_str =""
#for i in range(1,n+1):
#    suma += i
#    suma_str += str(i)
#    if i<n:
#        suma_str += (" + ")
#print(f"La suma de los numeros desde 1 hasta {n} es: {suma_str} = {suma}")

#13

#n = int(input("Ingrese un numero natural: "))
#suma = 0
#for i in range(2,2*n+1,2):
#    suma += i
#print(f"La suma de los primeros {n} numeros pares es: {suma}")

#14

#num1 = int(input("Ingrese un numero: "))
#num2 = int(input("Ingrese otro numero: "))
#for i in range(num1+1,num2):
#    if i%2==0:
#        print(i)

#15

#numero = int(input("Ingrese un número entero: "))
#if numero>1:
#    for i in range(2, numero):
#        if (numero % i) == 0:
#            print(f"{numero} no es primo")
#            break
#    else:
#        print(f"{numero} es primo")
#else:
#    print(f"{numero} no es primo")

