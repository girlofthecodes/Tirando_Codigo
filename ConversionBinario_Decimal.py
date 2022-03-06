
#Ejercicio 3
print("Calcula las siguientes sumas de numeros codificados con 8 bits en el sistema posicional.")
print("""
      a. 01111111 + 00000001 
      b. 01010101 + 10101010 
      c. 00000011 + 00000001""")
print("\nMETODO EXTENDIDO")
print("\nNumeros binarios: ")
valor_numerico1 = '01111111' 
valor_numerico2 = '00000001'
print(valor_numerico1, "-", valor_numerico2)

numero_decimal1 = 0
numero_decimal2 = 0

print("\nLongitud de los numeros binarios")
posicion_binario1 = len(valor_numerico1) - 1 #posición del primer digito por la izquierda
posicion_binario2 = len(valor_numerico2) - 1
print(posicion_binario1, "-", posicion_binario2)

print("\nRecorriendo los numeros binarios")
print(f"Binario: {valor_numerico1}")
for valor_string1 in valor_numerico1: 
    digito1 = int(valor_string1) 
    print(digito1)
print()
print(f"Binario: {valor_numerico2}")
for valor_string2 in valor_numerico2: 
    digito2 = int(valor_numerico2)
    print(digito2)

print("\nPosicion que ocupa cada binario del numero completo")
for valor_string1 in valor_numerico1: 
    digito1 = int(valor_string1) 
    print(f"Digito: {digito1}, Posicion: {posicion_binario1}")
    posicion_binario1 -= 1 #posicion = posicion - 1
print()
for valor_string2 in valor_numerico2: 
    digito2 = int(valor_numerico2)
    print(f"Digito: {digito2}, Posicion: {posicion_binario2}")
    posicion_binario2 -= 1
    
print("\nRecorriendo los binarios inversamente")
for posicion_binario1, valor_string1 in enumerate(valor_numerico1[::-1]):
    digito1 = int(valor_string1) 
    print(f"Digito: {digito1}, Posicion: {posicion_binario1}")
print()
for posicion_binario2, valor_string2 in enumerate(valor_numerico2[::-1]):
    digito2 = int(valor_string2) 
    print(f"Digito: {digito2}, Posicion: {posicion_binario2}")

print("\nMultiplica cada digito y eleva a su posicion")
for posicion_binario1, valor_string1 in enumerate(valor_numerico1[::-1]):
    digito1 = int(valor_string1)
    multiplicacion1 = digito1 * 2 ** posicion_binario1
    print(f"Digito: {digito1}, Posicion: {posicion_binario1}, Multiplicacion: {multiplicacion1}")
print()
for posicion_binario2, valor_string2 in enumerate(valor_numerico2[::-1]):
    digito2 = int(valor_string2)
    multiplicacion2 = digito2 * 2 ** posicion_binario2
    print(f"Digito: {digito2}, Posicion: {posicion_binario2}, Multiplicacion: {multiplicacion2}")

print("\nSumar el resultado de todas las operaciones")
for posicion_binario1, valor_string1 in enumerate(valor_numerico1[::-1]):
    numero_decimal1 += int(valor_string1) * 2 ** posicion_binario1
print(f"El decimal del equivalente binario {valor_numerico1} es {numero_decimal1}")
print()
for posicion_binario2, valor_string2 in enumerate(valor_numerico2[::-1]): 
    numero_decimal2 = int(valor_string2) * 2 ** posicion_binario2
print(f"El decimal del equivalente binario {valor_numerico2} es {numero_decimal2}")

print("\nSuma de ambos binarios convertidos a decimales")
suma_decimal = numero_decimal1 + numero_decimal2
print(f"La suma de los decimales {numero_decimal1} + {numero_decimal2}: {suma_decimal}")

print("\nMETODO SIMPLIFICADO CON CLAUSULAS DE PYTHON")
print("Ejercicio resuelto del inciso (a)")
binarioa1 = int('01111111',2)  
binarioa2 = int('00000001',2)
suma_binarioa = binarioa1 + binarioa2
print(f"La suma de los binarios {valor_numerico1} y {valor_numerico2}: {suma_binarioa}")
print("\nEjercicio resuelto del inciso (b)")
binariob1 = int('01010101',2)
binariob2 = int('10101010',2)
suma_binariob = binariob1 + binariob2
print(f"La suma de los binarios 01010101 y 10101010: {suma_binariob}")
print("\nEjercicio resuelto del inciso (c)")
binarioc1 = int('00000011',2)
binarioc2 = int('00000001',2)
suma_binarioc = binarioc1 + binarioc2
print(f"La suma de los binarios 00000011 y 00000001: {suma_binarioc}")
