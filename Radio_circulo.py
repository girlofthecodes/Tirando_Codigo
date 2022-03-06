#Ejercicio 9 
from math import pi 
print("""
Diseña un algoritmo para calcular el area de un circulo dado su radio. (Recuerda que el area de un circulo es 
π veces el cuadrado del radio.)
""")
radio = float(input("Radio del circulo: "))
area = pi * radio ** 2
print(f"Area del circulo: {area}")