print("""
Diseña un programa que indique si una cadena leída de teclado está bien formada como numero entero. El programa
escribiría ✭✭Es entero✮✮ en caso afirmativo y ✭✭No es entero✮✮ en caso contrario.
Por ejemplo, para ’12’ mostrará ✭✭Es entero✮✮, pero para ’1 2’ o ’a’ mostrará ✭✭No es entero✮✮
""")
cadena = input("Dime un número a evaluar: ")
for i in len(cadena): 
    if cadena == '':
        print("Hay un espacio") 
