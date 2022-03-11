#Ejercicio 112
print("""
Diseña un programa que solicite la lectura de un numero entre 0 y 10 (ambos inclusive). Si el usuario teclea un
numero fuera del rango valido, el programa solicitara nuevamente la introduccion del valor cuantas veces sea menester.
""")
numero = int(input("Numero a evaluar: "))
while numero < 0  or numero > 10: 
    print(f"{numero} se encuentra fuera del rango permitido")
    numero = int(input("Numero a evaluar: "))
else: 
    print(f"{numero} dentro del rango permitido")
    
#Ejercicio 113
print("""
El programa anterior pide el valor del radio al principio y, despues, permite seleccionar uno o mas calculos con ese
valor del radio. Modifica el programa para que pida el valor del radio cada vez que se solicita efectuar un nuevo calculo
""")
from math import pi 
radio = float(input("Ingresa el radio del circulo: "))
print("""
-----Menú-----
Escoge una opcion: 
a. Perimetro del Circulo
b. Area del Circulo
c. Exit
""")
opcion = input("¿Que quieres realizar? ")
while opcion == 'a' or opcion == 'b':
    if opcion == 'a': 
        perimetro = 2 * pi * radio
        print(f"El perimetro del circulo es de {round(perimetro, 2)}")
        continuar = input("¿Quieres volver a hacer el calculo (y / n)? ")
        if continuar == 'y': 
            radio = float(input("Ingresa el radio del circulo: "))
            print("""
            -----Menú-----
            Escoge una opcion: 
            a. Perimetro del Circulo
            b. Area del Circulo
            c. Exit
            """)
            opcion = input("¿Que quieres realizar? ")
        elif continuar == 'n': 
            print("""
            -----Menú-----
            Escoge una opcion: 
            a. Perimetro del Circulo
            b. Area del Circulo
            c. Exit
            """)
            opcion = input("¿Que quieres realizar? ")
        else: 
            print("Caracter invalido")
            break
    elif opcion == 'b': 
        area = pi * radio ** 2
        print(f"El area del circulo es de {round(area, 2)}")
        continuar = input("¿Quieres volver a hacer el calculo (y / n)? ")
        if continuar == 'y': 
            radio = float(input("Ingresa el radio del circulo: "))
            print("""
            -----Menú-----
            Escoge una opcion: 
            a. Perimetro del Circulo
            b. Area del Circulo
            c. Exit
            """)
            opcion = input("¿Que quieres realizar? ")
        elif continuar == 'n': 
            print("""
            -----Menú-----
            Escoge una opcion: 
            a. Perimetro del Circulo
            b. Area del Circulo
            c. Exit
            """)
            opcion = input("¿Que quieres realizar? ")   
        else: 
            print("Caracter invalido")
            break
print()

#Ejercicio 135
print("""
Haz un programa que vaya leyendo numero hasta que el usuario introduzca un numero negativo. En ese momento,
el programa mostrara por pantalla el numero mayor de cuantos ha visto.
""")
numero = int(input("Numero: "))
listaNumeros = [] 
listaNumeros.append(numero)
while numero >= 0:
    print("Para salir del ciclo, ingresa un valor negativo")
    numero = int(input("Numero: ")) 
    listaNumeros.append(numero)
else:
    print("Haz salido del ciclo")
    
del(listaNumeros[-1])
listaNumeros.sort()
print(listaNumeros)
