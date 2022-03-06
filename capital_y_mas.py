#Ejercicio 39
print("""
Haz un programa que pida al usuario una cantidad de euros, una tasa de interes y un numero de años. Muestra
por pantalla en cuanto se habra convertido el capital inicial transcurridos esos años si cada año se aplica la tasa de 
interes introducida.
Recuerda que un capital de C euros a un interes del x por cien durante n años se convierten en C · (1 + x/100)n euros.
(Prueba tu programa sabiendo que una cantidad de 10 000 E al 4.5% de interes anual se convierte en 24 117.14 E al cabo
de 20 años.)
""")
euros = float(input("Euros: "))
interes = float(input("Interes: "))
años = int(input("Años: "))
capital = (euros * (1 + interes/100) ** años)
print('Usted paraga en {} años un total de {} euros'.format(años, round(capital,2)))

#Ejercicio 40
print("""\nHaz un programa que pida el nombre de una persona y lo muestre en pantalla repetido 1000 veces, pero dejando 
un espacio de separacion entre aparicion y aparicion del nombre. (Utiliza los operadores de concatenacion 
y repeticion.)
""")
nombre = input("Dime tu nombre: ")
cadena = nombre + " "
print(cadena * 1000)