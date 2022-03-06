#Ejercicio 20
print("""
Evaluaa el polinomio x4 + x3 + 2x2 − x en x = 1.1. Utiliza variables para evitar teclear varias veces el valor de x. 
""")
x = 1.1
polinomio = x**4 + x**3 + 2*(x)**2 - x
print(f"El resultado de realizar el polinomio es: {polinomio}") #4.1151

#Ejercicio 21
print("\nEvalua el polinomio x4 + x3 +12x2 − x en x = 10. Asegurate de que el resultado sea un numero flotante.")
x = 10.0
polinomio = (x)**4 + (x)**3 + (1/2*(x)**2) - x 
print(f"El resultado de realizar el polinomio es: {polinomio}") #11040.0

#Ejercic""io 22
print("""\n¿Que resultara de ejecutar las sigueintes sentencias? 
    a. z = 2
    b. z += 2
    c. z += 2 - 2
    d. z *= 2
""")
z = 2
print(z) #2
z += 2
print(z) #4
z +=  2 - 2 
print(z) #4
z *= 2 
print(z) #8 
#Z almacena el ultimo valor que se guarda en la memoria de la variable, si se inicializa los incisos c = 2 y d = 4
z *= 1 + 1
print(z) #9
z /= 2
print(z) #3.5
z %= 3
print(z) #1
z /= 3 - 1
print(z) #-0.666
z -= 2 + 1
print(z)
z -= 2
print(z)
z **= 3
print(z)
