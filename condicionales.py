
    
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