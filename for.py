#Ejercicio 117 
print("""
Haz un programa que muestre la tabla de multiplicar de un numero introducido por teclado por el usuario. Aqui
tienes un ejemplo de como se debe comportar el programa:
Dame un nuumero: 5
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
""")
numero = int(input("Ingresa el numero de cual quieres ver la tabla de multiplicar: "))
for i in range(1, 11): 
    print(f"{numero} x {i} = {numero * i}")
print()

#Ejercicio 120 
print("""
Haz un programa que muestre, en lineas independientes, todos los numeros pares comprendidos entre 0 y 200 (ambos
inclusive).
""")
for i in range(0, 201, 2): 
    print(f"El numero {i} es un numero par")
print()

#Ejercicio 121
print("""
Haz un programa que muestre, en lineas independientes y en orden inverso, todos los numeros pares comprendidos
entre 0 y 200 (ambos inclusive).
""")

for i in range(200, 0, -2): 
    print(f"El numero {i} es un numero par")
print()

#Ejercicio 122
print("""
Escribe un programa que muestre los numeros pares positivos entre 2 y un numeros cualquiera que introduzca el
usuario por teclado.
""")
numero = int(input("Ingresa el numero: "))
print(f"A continuación se mostrara los numeros pares que preceden al {numero}")
for i in range(2, numero + 1, 2): 
    print(f"{i}")
print()

#Ejercicio 122
print("""
Haz un programa que pida el valor de dos enteros n y m y calcule el sumatorio de todos los numero pares
comprendidos entre ellos (incluyendolos en el caso de que sean pares).
""")

n = int(input("Valor numero 1: "))
m = int(input("Valor numero 2: "))
suma = 0
print(f"Numeros pares de {n} a {m}")
for i in range(n, m+1, 2): 
    print(f"{i}")
print()

for s in range(n, m+1, 2): 
    suma = suma + s
    print(suma)
print()

