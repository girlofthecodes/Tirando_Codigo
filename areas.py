from math import sqrt, radians, sin, pi
#Ejercicio 31
print("""
Diseña un programa que, a partir del valor del lado de un cuadrado (3 metros), muestre el valor de su perimetro (en
metros) y el de su area (en metros cuadrados).
(El perimetro debe darte 12 metros y el area 9 metros cuadrados.)
""")
lado = 3 #metros
perimetro = lado * 4
area = lado * lado 
print(f"Perimetro: {perimetro}, Area: {area}")

#Ejercicio 32
print("""\n
Diseña un programa que, a partir del valor de la base y de la altura de un triangulo (3 y 5 metros, respectivamente),
muestre el valor de su area (en metros cuadrados).
Recuerda que el area A de un triangulo se puede calcular a partir de la base b y la altura h como A =1/2bh 
(El resultado es 7.5 metros cuadrados.)     
""")
base = 3
altura = 5
area = base * altura / 2
print(f"Area: {area}")

#Ejercicio 33
print("""\n
Diseña un programa que, a partir del valor de los dos lados de un rectangulo (4 y 6 metros, respectivamente), muestre
el valor de su perimetro (en metros) y el de su area (en metros cuadrados).
(El perimetro debe darte 20 metros y el area 24 metros cuadrados.)
""")
lado1 = 4
lado2 = 6
perimetro = lado1 * 2 + lado2* 2
area = lado1 * lado2
print(f"Perimetro: {perimetro}, Area: {area}")

#Ejercicio 34
print("""\n
Diseña un programa que pida el valor del lado de un cuadrado y muestre el valor de su perimetro y el de su area.
(Prueba que tu programa funciona correctamente con este ejemplo: si el lado vale 1.1, el perimetro sera 4.4, y el area
1.21.)
""")
lado = float(input("Lado del cuadrado: "))
perimetro = lado * 4
area = lado * lado
print(f"Perimetro: {perimetro}, Area: {area}")

#Ejercicio 35
print("""\nDiseña un programa que pida el valor de los dos lados de un rectangulo y muestre el valor de su perimetro y el 
de su area.(Prueba que tu programa funciona correctamente con este ejemplo: si un lado mide 1 y el otro 5, el perimetro 
seria 12.0, y el area 5.0.)
""")
lado1 = float(input("Altura del rectangulo: "))
lado2 = float(input("Base del rectangulo: "))
perimetro = lado1 * 2 + lado2 * 2
area = lado1 * lado2
print(f"Permietro: {perimetro}, Area: {area}")

#Ejercicio 36
print("""\nDiseña un programa que pida el valor de la base y la altura de un triangulo y muestre el valor de su area.
(Prueba que tu programa funciona correctamente con este ejemplo: si la base es 10 y la altura 100, el area seria 500.0.)
""")
base = int(input("Base del triangulo: "))
altura = int(input("Altura de un triangulo: "))
area = base * altura / 2 
print(f"Permietro: {perimetro}, Area: {area}")

#Ejercicio 37
print("""\nDiseña un programa que pida el valor de los tres lados de un triangulo y calcule el valor de su area y 
perimetro.Recuerda que el area A de un triangulo puede calcularse a partir de sus tres lados, a, b y c, asi: 
A =(raiz cuadrada) s(s-a)(s-b)(s-c) donde s = (a + b + c)/2 (Prueba que tu programa funciona correctamente con este 
ejemplo: si los lados miden 3, 5 y 7, el perimetro seria 15.0 y el area 6.49519052838.)
""")
ladoa = int(input("Lado A del triangulo: "))
ladob = int(input("Lado B del triangulo: "))
ladoc = int(input("Lado C del triangulo: "))
perimetro = ladoa + ladob + ladoc
s = (ladoa + ladob + ladoc) / 2
area = sqrt(s * (s - ladoa) * (s - ladob) * (s - ladoc))
print(f"Perimetro: {perimetro}, Area: {area}")

#Ejercicio 38 
print("""\nEl area A de un triangulo se puede calcular a partir del valor de dos de sus lados, a y b, y del triangulo
θ que estos forman entre si con la formula A =1/2ab sin(θ). Diseña un programa que pida al usuario el valor de los dos 
lados (en metros), el triangulo que estos forman (en grados), y muestre el valor del area. 
(Ten en cuenta que la funcion sin de Python trabaja en radianes, asi que el triangulo que leas en grados deberias pasarlo 
a radianes sabiendo que π radianes son 180 grados. Prueba que has hecho bien el programa introduciendo los siguientes 
datos: a = 1, b = 2, θ = 30; el resultado es 0.5.)
""")
ladoa = float(input("Lado A del triangulo: "))
ladob = float(input("Lado B del triangulo: ")) 
angulo = float(input("Angulo que forman los lados A y B del triangulo: "))
#radians -> Convierte de grados a radianes 
#degress -> Convierte de radianes a grados
radianes = radians(angulo)
area = 1/2 * (ladoa) * (ladob) * sin(radianes)
print("Area del triangulo: ", round(radianes, 1))

#Ejercicio 45
print("""\nDiseña un programa que solicite el radio de una circunferencia y muestre su area y perimetro con 
solo 2 decimales.""")
radio = float(input("Radio del circulo: "))
perimetro = 2 * pi * radio
area = pi * radio ** 2
print("Perimetro: ", round(perimetro, 2), "Area: ", round(area, 2))