#Ejercicio 7
print("""Diseña un programa que calcule la media de cinco numeros señalados por el usuario, 
de igual forma de manera en la que en el programa se encuentren los datos
""")
print("\nDatos pos salida")
x1 = 10
x2 = 45
x3 = 12
x4 = 34
x5 = 5
suma_datos = x1 + x2 + x3 + x4 + x5
media = suma_datos / 5
print(f"La media es un total de: {media}")
print("\nDatos por entrada")
for i in range(1, 6): 
    datos = int(input(f"Ingresa el valor {i}: "))
    suma_datos = i + i
    media = suma_datos / 5
print(f"La media es un total de: {media}")