# 1

#a

#print("Las máquinas me sorprenden con mucha frecuencia.")

#b

#print()

#c

#print("Hola Mundo")

#d

#print("23", 23)        El "23" se muestra como un string.

#e

#print("Una computadora puede ser llamada ""inteligente"" si logra engañar a una persona haciéndole creer que es un humano.” Las comillas que encierran a la palabra inteligente deben imprimirse.")

#f

#print("Ramiro", "Silva", "20")

#g

#print("Ramiro", "Silva", "20", sep="_")

#h

#print("Calle\t", "Numero\t", "Codigo")

#i

#print("Calle\n", "Numero\n", "Codigo")

#j

#var="Feliz\n\tPrimavera\n\t\t2023"
#print(var)

#k

#print("Solo podemos ver poco del futuro,", end=" ")
#print("pero lo suficiente para darnos cuenta de que hay mucho que hacer")

#l

#print("    *")
#print("   * *")
#print("  * * *")
#print(" * * * *")
#print("*** *** ***")
#print("   * *")
#print("   * *")
#print("  *****")

#3 y 4

#a

#nombre     String

#b

#apellido       String

#c

#edad       Int


#d

#altura     Int

#e

#num_vuelo      Int

#f

#temp_ambiente      Int

#g

#salario_mensual        Float

#h

#termino_juego      Boolean

#i

#es_par     Boolean

#5

#a

#nombre = input("Ingrese su nombre: ")
#apellido = input("Ingrese su apellido: ")
#edad = input("Ingrese su edad: ")
#print(f"{nombre} {apellido}, ser creativo a los {edad} años.")

#b

#nombre = input("Ingrese su nombre: ")
#apellido = input("Ingrese su apellido: ")
#edad = input("Ingrese su edad: ")

#mensaje_creativo = f"{nombre} {apellido}, ser creativo a los {edad} años."
#input(mensaje_creativo)

#6

#numero1 = int(input("Ingrese el primer número entero: "))
#numero2 = int(input("Ingrese el segundo número entero: "))
#suma = numero1 + numero2
#resta = numero1 - numero2
#producto = numero1 * numero2
#potencia = numero1 ** numero2
#resto = numero1 % numero2

#7

#numero_entero = int(input("Ingrese un número entero: "))
#numero_float = float(input("Ingrese un número decimal (float): "))
#suma = numero_entero + numero_float
#resta = numero_entero - numero_float
#producto = numero_entero * numero_float
#potencia = numero_entero ** numero_float
#resto = numero_entero % numero_float

#8

#base_rectangulo = float(input("Ingrese la base del rectángulo: "))
#altura_rectangulo = float(input("Ingrese la altura del rectángulo:"))
#perimetro_rectangulo = 2 * (base_rectangulo + altura_rectangulo)
#area_rectangulo = base_rectangulo * altura_rectangulo
#print(f"Rectángulo - Perímetro: {perimetro_rectangulo}, Área: {area_rectangulo}")

#radio_circunferencia = float(input("Ingrese el radio de la circunferencia: "))
#pi = 3.14
#perimetro_circunferencia = 2 * pi * radio_circunferencia
#area_circunferencia = pi * radio_circunferencia ** 2
#print(f"Circunferencia - Perímetro: {perimetro_circunferencia}, Área: {area_circunferencia}")

#9

#peso = float(input("Ingrese su peso: "))
#estatura = float(input("Ingrese su estatura: "))
#imc = peso/(estatura*estatura)
#print(f"Tu indice de masa corporal es: {imc}")

#10

#temp = float(input("Ingrese una temperatura en °C: "))
#conversion = (temp*1.8)+32
#print(f"La temperatura en °F es: {conversion}")

#11

#horas = int(input("Ingrese las horas trabajadas: "))
#costo_hora = int(input("Ingrese el costo por hora: "))
#sueldo = horas*costo_hora
#print(f"El sueldo es: {sueldo}")

#12

#cantidad = float(input("Ingrese la cantidad a invertir: "))
#interes_anual = float(input("Ingrese el interes anual: "))
#años = int(input("Ingrese el numero de años: "))
#rendimiento = (cantidad*interes_anual*años)/100
#capital = cantidad+rendimiento
#print(f"El capital final es: {capital}")

#13

#precio1 = float(input("Ingrese el precio del producto 1: "))
#precio2 = float(input("Ingrese el precio del producto 2: "))
#precio3 = float(input("Ingrese el precio del producto 3: "))
#precio4 = float(input("Ingrese el precio del producto 4: "))
#precio5 = float(input("Ingrese el precio del producto 5: "))
#precio6 = float(input("Ingrese el precio del producto 6: "))
#precio7 = float(input("Ingrese el precio del producto 7: "))
#precio8 = float(input("Ingrese el precio del producto 8: "))
#precio9 = float(input("Ingrese el precio del producto 9: "))
#precio10 = float(input("Ingrese el precio del producto 10: "))
#promedio = (precio1 + precio2 + precio3 + precio4 + precio5 + precio6 + precio7 + precio8 + precio9 + precio10)/10
#print(f"El promedio de los precios es: {promedio}")

#14

#concatenar = 'Una ambiciosa' + ' Introducción' + ' a Python' + ' Parte 1'
#print(concatenar)

#15

#a

#sociedad = 'aiPython P1'
#print(sociedad)

#b

#print(len(sociedad))

#c

#print(sociedad.upper())

#d

#print(sociedad.lower())

#16

#string = "sometimes it is the people no one imagines anything of who do the things that no one can imagine."
#string_formateado = string.capitalize().title().swapcase()
#print(string_formateado)

#17

#nombre = input("Ingrese su nombre: ")
#print(f"{nombre} {nombre} {nombre}")

#18

#print("        *")
#print("       * *")
#print("      * * *")
#print("     * * * *")
#print("    * * * * *")
#print("   * * * * * *")
#print("  * * * * * * *")
#print(" * * * * * * * *")
#print("*** *** *** *** ***")
#print("      * * *")
#print("      * * *")
#print("     *****")

#19

#print("        *"
#      "\n       * *"
#      "\n      * * *"
#      "\n     * * * *"
#      "\n    * * * * *"
#      "\n   * * * * * *"
#      "\n  * * * * * * *"
#      "\n * * * * * * * *"
#      "\n*** *** *** *** ***"
#      "\n      * * *"
#      "\n      * * *"
#      "\n     *****")

#20

#print("        *\t\t        *"
#      "\n       * *\t\t       * *"
#      "\n      * * *\t\t      * * *"
#      "\n     * * * *\t\t     * * * *"
#      "\n    * * * * *\t\t    * * * * *"
#      "\n   * * * * * *\t   * * * * * *"
#      "\n  * * * * * * *\t  * * * * * * *"
#      "\n * * * * * * * *\t * * * * * * * *"
#      "\n*** *** *** *** ***\t*** *** *** *** ***"
#      "\n      * * *\t\t      * * *"
#      "\n      * * *\t\t      * * *"
#      "\n     *****\t\t     *****")

#21

#palabra = input("Ingrese una palabra: ")
#resultado = palabra.replace('a', '😀')
#print(f"Palabra modificada: {resultado}")

#22

#frase = "El razonamiento matemático puede considerarse más bien esquemáticamente como el ejercicio de una combinación de dos instalaciones, que podemos llamar la intuición y el ingenio."
#palabras = frase.split()
#primeras_palabras = ' '.join(palabras[:2])
#print(f"Dos primeras palabras: {primeras_palabras}")

#23

#frase = " La ciencia es una ecuación diferencial. La religión es una condición de frontera. "
#frase_sin_espacios = frase.strip()
#print(f"Frase sin espacios: {frase_sin_espacios}")

#24

#frase = "La ciencia es una ecuación diferencial. La religión es una condición de frontera."
#frase_separada = "La ciencia es una ecuación diferencial.\nLa religión es una condición de frontera."
#print(f"Frase separada:\n{frase_separada}")

#25

#nombre = "Alexa"
#edad = 25
#pais = "USA"
#ciudad = "CapeCod"
#print(f"Nombre\tEdad\tPais\tCiudad")
#print(f"{nombre}\t{edad}\t{pais}\t{ciudad}")



