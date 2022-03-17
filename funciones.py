print("""
Solicitar al usuario que ingrese su dirección email. Imprimir un mensaje indicando si la dirección es válida o no, valiéndose de una 
función para decidirlo. Una dirección se considerará válida si contiene el símbolo "@".
""")
def Email():
    email = input("Ingresa tu correo electronico: ")
    if '@' in email: 
        print("El correo ingresado es valido")
    else: 
        print("Sintaxis de correo requerida invalida")

Email()
print()

print("""
- Solicitar números al usuario hasta que ingrese el cero. Por cada uno, mostrar la suma de sus dígitos (utilizando una función que realice 
dicha suma).
""")
def Suma(): 
    suma = 0
    numero = int(input("ingresa un numero: "))
    while numero != 0: 
        suma += numero
        print(f"La suma es de {suma}")
        numero = int(input("Ingresa un numero:"))
    
        
Suma()
print()

print("""
Solicitar números al usuario hasta que ingrese el cero. Por cada uno, mostrar la suma de sus dígitos. Al finalizar, mostrar la 
sumatoria de todos los números ingresados y la suma de sus dígitos. Reutilizar la misma función realizada en el ejercicio 2.
""")
def suma(): 
    suma = 0
    numero = int(input("Ingresa un numero: "))
    while numero != 0: 
        suma += numero
        print(f"La suma actual es de {suma}")
        numero = int(input("Ingresa un numero: "))

    print(f"La suma total es de {suma}")
    sumDigit, extNum = 0, 0 
    while suma != 0:
        extNum = suma % 10
        suma //= 10
        sumDigit += extNum
    print(f"La suma de los digitos que conforman la suma total es de: {sumDigit}")
suma()
print()

print("""
Requerir al usuario que ingrese un número entero e informar si es primo o no, utilizando una función booleana que lo decida.
""")
def Primo():
    numero = int(input("Ingresa un numero: "))
    while numero != 1: 
        for i in range(2, numero): 
            if numero % i == 0:
                print(f"No es primo, {i} es divisor") 
                return False
        print(f"{numero} es primo")
        return True
    else: 
        print("El 1 no es primo")

Primo()
print()

print("""
Solicitar al usuario un número entero y luego un dígito. Informar la cantidad de ocurrencias del dígito en el número, utilizando 
para ello una función que calcule la frecuencia.
""")    
print()

print("""

Escribir un programa que pida números al usuario, mostrar el factorial de cada uno y, al finalizar, la cantidad total de números leídos en 
total. Utilizar una o más funciones, según sea necesario.""")
from math import factorial
def Factorial(num): 
    total_numeros = int(input("¿Cuantos numeros deseas ingresar? "))
    for i in range(1, total_numeros + 1): 
        numero = int(input(f"Ingresa el valor del numero {i}: "))
        print(f"El factorial de {numero} es {factorial(numero)}")
        print("\nSegunda forma de sacar el factorial x!")
        print(f"El factorial de {num} es {factorial(num)}")

Factorial(5)
print()
print("""
- Escribir un programa que pida números positivos al usuario. Mostrar el número cuya sumatoria de 
dígitos fue mayor y la cantidad de números cuya sumatoria de dígitos fue menor que 10. Utilizar 
una o más funciones, según sea necesario.
""")
def SumaDigitos(): 
    total_numeros = int(input("Ingresa la cantidad de numeros que se evaluarán: "))
    lista_max = []
    for i in range(1, total_numeros + 1): 
        numero = int(input(f"Ingresa el valor del numero {i}: "))
        if numero > 0: 
            sumDigit, extNum = 0, 0 
            while numero != 0:
                extNum = numero % 10
                numero //= 10
                sumDigit += extNum
            lista_max.append(sumDigit)        
        print(lista_max)
        mayor = lista_max[0]
        for x in range(len(lista_max)): 
            if lista_max[x] > mayor: 
                mayor = lista_max[x]
                print(f"Suma de los digitos mayor: {mayor}")
    
        menor = 10
        for i in range(len(lista_max)): 
            if lista_max[i] < menor:
                menor = lista_max[i] 
                print("La suma de los digitos  < 10: ", menor)

SumaDigitos()
print()

print("""
Solicitar al usuario el ingreso de números primos. La lectura finalizará cuando ingrese un número 
que no sea primo. Por cada número, mostrar la suma de sus dígitos. También solicitar al usuario 
un dígito e informar la cantidad de veces que aparece en el número (frecuencia). Al finalizar el 
programa, mostrar el factorial del mayor número ingresado.
""")
print("""
Solicitar al usuario el ingreso de números primos. La lectura finalizará cuando ingrese un número 
que no sea primo. Por cada número, mostrar la suma de sus dígitos. También solicitar al usuario 
un dígito e informar la cantidad de veces que aparece en el número (frecuencia). Al finalizar el 
programa, mostrar el factorial del mayor número ingresado.
""")
from math import factorial
def is_Prime(): 
    lista_numeros = []
    numeros_ingresar = int(input("Numeros a ingresar: "))
    for x in range(1, numeros_ingresar + 1): 
        numero = int(input(f"Ingresa el valor del numero {x}: "))
        for i in range(2, numero): 
            if numero % i != 0:
                print(f"{numero} es primo")
                if numero > 0: 
                    sumDigit, extNum = 0, 0 
                    while numero != 0:
                        extNum = numero % 10
                        numero //= 10
                        sumDigit += extNum
                    lista_numeros.append(sumDigit)        
                    print(lista_numeros)
                    mayor = lista_numeros[0]
                    for max in range(len(lista_numeros)): 
                        if lista_numeros[max] > mayor: 
                            mayor = lista_numeros[max]
                            print(f"La suma de los digitos tiene como mayor a {mayor}")
            else:
                break
            
    print(f"El factorial del numero mayor de la suma de los digitos es {factorial(mayor)}")             
            
is_Prime()
