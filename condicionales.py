#Ejercicio 58
print("""Diseña un programa que lea un numero flotante por teclado y muestre por pantalla el mensaje 'El numero es
negativo.' solo si el numero es menor que cero.
""")
numero = float(input("Numero: "))
if numero < 0: 
    print("El numero es negativo")

#Ejercicio 59
print("""\nDiseña un programa que lea un numero flotante por teclado y muestre por pantalla el mensaje 'El numero es
positivo' solo si el numero es mayor o igual que cero. 
""")
numero = float(input("Numero: "))
if numero >= 0: 
    print("El numero es positivo")

#Ejercicio 60
print("""\nDiseña un programa que lea la edad de dos personas y diga quién es más joven, la primera o la segunda. 
Ten en cuenta que mabas pueden tener la misma edad. En tal caso, hazlo saber con un mensaje adecuado. 
""")
edad1 = int(input("Edad de la persona 1: "))
edad2 = int(input("Edad de la persona 2: "))
if edad1 == edad2: 
    print("Ambas personas tienen la misma edad")
elif edad1 < edad2: 
    print("La persona 2 es mayor que la persona 1")
elif edad1 > edad2: 
    print("La persona 1 es mayor que la persona 2")
else: 
    print("Haz introducido 0 o cualquier otro caracter invalido")

#Ejercicio 61
print("""\nDiseña un programa que lea un cáracter de teclado y muestre por pantalla el mensjae 'Es parentesis' solo si 
el caracter leido es un parentesis abierto o cerrado. 
""")
caracter = input("Caracter a evaluar: ")
if caracter == "(": 
    print("Es parentesis abierto")
elif caracter == ")": 
    print("Es parentesis cerrado") 
else: 
    print("Otro tipo de caracter")
    
#Ejercicio 64
print("""\nDiseña un programa que, dado un numero entero, muestre por pantalla el mensaje 'El numero es par.' cuando el
numero sea par y el mensaje 'El numero es impar.' cuando sea impar.
(Una pista: un numero es par si el resto de dividirlo por 2 es 0, e impar en caso contrario.)
""")
numero = int(input("Numero a evaluar: "))
if numero % 2 == 0: 
    print(f"El numero {numero} es par")
else: 
    print(f"El numero {numero} es impar")
    
#Ejercicio 65
print("""\nDiseña un programa que, dado un numero entero, determine si este es el doble de un numero impar. 
(Ejemplo: 14 es el doble de 7, que es impar.)
""")
numero = int(input("Numero a evaluar: "))
if numero % 2 == 0: 
    print(f"El numero {numero} es par")
elif numero % 22 != 0: 
    print(f"El numero {numero} es impar")

operacion = numero // 2
if (numero % 2 == 0) and (operacion % 2 != 0):
    print(f"{numero} es el doble de {operacion}, que es impar")
    
#Ejercicio 66
print("""\nDiseña un programa que, dados dos numeros enteros, muestre por pantalla uno de estos mensajes: 'El segundo
es el cuadrado exacto del primero.', 'El segundo es menor que el cuadrado del primero.' o 'El segundo es
mayor que el cuadrado del primero.', dependiendo de la verificacion de la condicion correspondiente al significado de
cada mensaje.
""")
numero1 = int(input("Numero 1: "))
numero2 = int(input("Numero 2: "))
if numero1 == numero2: 
    print("El segundo es el cuadrado exacto del primero")
elif numero1 > numero2: 
    print("El segundo es menor que el cuadrado del primero")
else: 
    print("El segundo es mayor que el cuadrado del primero")
    
#Ejercicio 67 
print("""\nUn capital de C euros a un interes del x por cien anual durante n años se convierte en C ·(1 + x/100)n euros. 
Diseña un programa Python que solicite la cantidad C y el interes x y calcule el capital final solo si x es una cantidad 
positiva.
""")
euros = float(input("Euros: "))
interes = float(input("Interes: "))
años = int(input("Años: "))
if interes > 0: 
    capital = euros * (1 + interes/100) ** años
    print('Usted paraga en {} años un total de {} euros'.format(años, round(capital,2)))
else: 
    print("No se puede sacar el calsulo, porque ingreso un valor negativo")
    
#Ejercicio 68
print("""\nRealiza un programa que calcule eel desglose en billetes y monedas de una cantidad exacta en euros. 
Hay billetes de 500, 200, 1oo, 50, 20, 10 y 5 y monedas de 2 y 1E
""")
euros = int(input("Monto del despliegue a calcular: "))
b500 = euros // 500; b500i = euros % 500
b200 = b500i // 200; b200i = b500i % 200
b100 = b200i // 100; b100i = b200i % 100
b50 = b100i // 50; b50i = b100i % 50
b20 = b50i // 20; b20i = b50i % 20
b10 = b20i // 10; b10i = b20i % 10
b5 = b10i // 5; b5i = b10i % 5
b2 = b5i // 2; b2i = b5i % 2
b1 = b2i // 1; b1i = b2i % 1

if b500 >= 1:
    print(str(b500) + " billete" + ('s' if (b500) > 1 else '') + " de 500")
if b200 >= 1:
    print(str(b200) + " billete" + ('s' if (b200) > 1 else '') + " de 200")
if b100 >= 1:
    print(str(b100) + " billete" + ('s' if (b100) > 1 else '') + " de 100")
if b50 >= 1:
    print(str(b50) + " billete" + ('s' if (b50) > 1 else '') + " de 50")
if b20 >= 1:
    print(str(b20) + " billete" + ('s' if (b20) > 1 else '') + " de 20")
if b10 >= 1:
    print(str(b10) + " billete" + ('s' if (b10) > 1 else '') + " de 10")
if b5 >= 1:
    print(str(b5) + " billete" + ('s' if (b5) > 1 else '') + " de 5")
if b2 >= 1:
    print(str(b2) + " moneda" + ('s' if (b2) > 1 else '') + " de 2")
if b1 >= 1:
    print(str(b1) + " moneda" + ('s' if (b1) > 1 else '') + " de 1")