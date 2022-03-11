print("""
Un vector en un espacio tridimensional es una tripleta de valores reales (x, y, z). Deseamos confeccionar un programa
que permita operar con dos vectores. 
+-----------------------------------------------+
|MENÚ                                              |
|1) Introducir el primer vector                 |
|2) Introducir el segundo vector                |   
|3) Calcular la suma                            |    
|4) Calcular la diferencia                      |
|5) Calcular el producto escalar                |
|6) Calcular el producto vectorial              |
|7) Calcular el angulo (en grados) entre ellos  |
|8) Calcular la longitud                        |
|9) Finaliza                                    |
+-----------------------------------------------+

Tras la ejecucion de cada una de las acciones del menu este reaparecera en pantalla, a menos que la opcion escogida sea
la numero 9. Si el usuario escoge una opcion diferente, el programa advertira al usuario de su error y el menu reaparecera.
Las opciones 4 y 6 del menu pueden proporcionar resultados distintos en funcion del orden de los operandos, asi que, si se
escoge cualquiera de ellas, debera mostrarse un nuevo menu que permita seleccionar el orden de los operandos. Por ejemplo,
la opcion 4 mostrara el siguiente menu:
+---------------------------------------+
|1) Primer vector menos segundo vector  |
|2) Segundo vector menos primer vector  |
+---------------------------------------+

Nuevamente, si el usuario se equivoca, se le advertira del error y se le permitira corregirlo.
La opcion 8 del menuu principal conducira tmabien a un submenu para que el usuario decida sobre cual de los dos vectores
se aplica el calculo de longitud.
Ten en cuenta que tu programa debe contemplar y controlar toda posible situacion excepcional: divisiones por cero, raices
con argumento negativo, etcetera. (Nota: La funcion arcocoseno se encuentra disponible en el modulo math y su identificador
es acos.)
""")
from math import acos, pi, sqrt
v1 = []
v2 = []
opcion = int(input("Ingresa la opcion a elegir: "))
while opcion != 9: 
    if opcion == 1: 
        for vector1 in range(1, 4): 
            elementosV1 = int(input(f"Ingresa el vector {vector1} del primer vector: "))
            v1.append(elementosV1)
        print(v1) #Temporales
        print("""
        +-----------------------------------------------+
        |MENÚ                                              |
        |1) Introducir el primer vector                 |
        |2) Introducir el segundo vector                |   
        |3) Calcular la suma                            |    
        |4) Calcular la diferencia                      |
        |5) Calcular el producto escalar                |
        |6) Calcular el producto vectorial              |
        |7) Calcular el angulo (en grados) entre ellos  |
        |8) Calcular la longitud                        |
        |9) Finaliza                                    |
        +-----------------------------------------------+
        """)
        opcion = int(input("Ingresa la opcion a elegir: "))
    elif opcion == 2: 
        for vector2 in range(1, 4): 
            elementosV2 = int(input(f"Ingresa el vector {vector2} del segundo vector: "))
            v2.append(elementosV2)
        print(v2) #Temporales
        print("""
        +-----------------------------------------------+
        |MENÚ                                           |
        |1) Introducir el primer vector                 |
        |2) Introducir el segundo vector                |   
        |3) Calcular la suma                            |    
        |4) Calcular la diferencia                      |
        |5) Calcular el producto escalar                |
        |6) Calcular el producto vectorial              |
        |7) Calcular el angulo (en grados) entre ellos  |
        |8) Calcular la longitud                        |
        |9) Finaliza                                    |
        +-----------------------------------------------+
        """)
        opcion = int(input("Ingresa la opcion a elegir: "))
    elif opcion == 3: 
        suma = v1[0] + v2[0], v1[1] + v2[1], v1[2] + v2[2]
        print(f"La suma de los vectoes es: {suma}")
        print("""
        +-----------------------------------------------+
        |MENÚ                                           |
        |1) Introducir el primer vector                 |
        |2) Introducir el segundo vector                |   
        |3) Calcular la suma                            |    
        |4) Calcular la diferencia                      |
        |5) Calcular el producto escalar                |
        |6) Calcular el producto vectorial              |
        |7) Calcular el angulo (en grados) entre ellos  |
        |8) Calcular la longitud                        |
        |9) Finaliza                                    |
        +-----------------------------------------------+
        """)
        opcion = int(input("Ingresa la opcion a elegir: "))
    elif opcion == 4: 
        print("""     
        +---------------------------------------+
        |1) Primer vector menos segundo vector  |
        |2) Segundo vector menos primer vector  |
        |3) Salir                               |
        +---------------------------------------+    
        """)
        s_opcion = int(input("¿Que operación quieres realizar? "))
        if s_opcion == 1: 
            diferencia = (v1[0] - v2[0], v1[1] - v2[1], v1[2] - v2[2])
            print(f"La diferencia de los vectores es: {diferencia}")
            print("""
            +-----------------------------------------------+
            |MENÚ                                           |
            |1) Introducir el primer vector                 |
            |2) Introducir el segundo vector                |   
            |3) Calcular la suma                            |    
            |4) Calcular la diferencia                      |
            |5) Calcular el producto escalar                |
            |6) Calcular el producto vectorial              |
            |7) Calcular el angulo (en grados) entre ellos  |
            |8) Calcular la longitud                        |
            |9) Finaliza                                    |
            +-----------------------------------------------+
            """)
            opcion = int(input("Ingresa la opcion a elegir: "))
        elif s_opcion == 2: 
            diferencia = (v2[0] - v1[0], v2[1] - v1[1], v2[2] - v1[2])
            print(f"La diferencia de los vectores es: {diferencia}")
            print("""
            +-----------------------------------------------+
            |MENÚ                                           |
            |1) Introducir el primer vector                 |
            |2) Introducir el segundo vector                |   
            |3) Calcular la suma                            |    
            |4) Calcular la diferencia                      |
            |5) Calcular el producto escalar                |
            |6) Calcular el producto vectorial              |
            |7) Calcular el angulo (en grados) entre ellos  |
            |8) Calcular la longitud                        |
            |9) Finaliza                                    |
            +-----------------------------------------------+
            """)
            opcion = int(input("Ingresa la opcion a elegir: "))
        elif s_opcion == 3: 
            break
        else: 
            print("Opcion no reconocida")
    elif opcion == 5: 
        producto_escalar = v1[0] * v2[0] + v1[1] * v2[1] + v1[2] * v2[2]
        print(f"El producto escalar de los vectores es de: {producto_escalar}")
        print("""
            +-----------------------------------------------+
            |MENÚ                                           |
            |1) Introducir el primer vector                 |
            |2) Introducir el segundo vector                |   
            |3) Calcular la suma                            |    
            |4) Calcular la diferencia                      |
            |5) Calcular el producto escalar                |
            |6) Calcular el producto vectorial              |
            |7) Calcular el angulo (en grados) entre ellos  |
            |8) Calcular la longitud                        |
            |9) Finaliza                                    |
            +-----------------------------------------------+
        """)
        opcion = int(input("Ingresa la opcion a elegir: "))
    elif opcion == 6: 
        print("""     
        +---------------------------------------+
        |1) Primer vector a segundo vector      |
        |2) Segundo vector a primer vector      |
        |3) Salir
        +---------------------------------------+    
        """)
        s_opcion = int(input("¿Que operación quieres realizar? "))
        if s_opcion == 1:         
            producto_vectorial = v1[1] * v2[2] - v1[2] * v2[1], v1[2] * v2[0] - v1[0] * v2[2], v1[0] * v2[1] - v1[1] * v2[0]
            print(f"El producto vectorial de los vectores es de: {producto_vectorial}")
            print("""
                +-----------------------------------------------+
                |MENÚ                                           |
                |1) Introducir el primer vector                 |
                |2) Introducir el segundo vector                |   
                |3) Calcular la suma                            |    
                |4) Calcular la diferencia                      |
                |5) Calcular el producto escalar                |
                |6) Calcular el producto vectorial              |
                |7) Calcular el angulo (en grados) entre ellos  |
                |8) Calcular la longitud                        |
                |9) Finaliza                                    |
                +-----------------------------------------------+
            """)
            opcion = int(input("Ingresa la opcion a elegir: "))
        elif s_opcion == 2: 
            producto_vectorial = v2[2] * v1[1] - v2[1] * v1[2], v2[0] * v1[2] - v2[2] * v1[0], v2[1] * v1[0] - v2[0] * v1[1]
            print(f"El producto vectorial de los vectores es de: {producto_vectorial}")
            print("""
                +-----------------------------------------------+
                |MENÚ                                           |
                |1) Introducir el primer vector                 |
                |2) Introducir el segundo vector                |   
                |3) Calcular la suma                            |    
                |4) Calcular la diferencia                      |
                |5) Calcular el producto escalar                |
                |6) Calcular el producto vectorial              |
                |7) Calcular el angulo (en grados) entre ellos  |
                |8) Calcular la longitud                        |
                |9) Finaliza                                    |
                +-----------------------------------------------+
            """)
            opcion = int(input("Ingresa la opcion a elegir: "))
        elif s_opcion == 3: 
            break
        else: 
            print("Opcion no reconocida")
    elif opcion == 7: 
        p1f = 180/ pi 
        p2f = (v1[0] * v2[0]) + (v1[1] * v2[1]) + (v1[2] * v2[2])
        p3f = sqrt((v1[0] ** 2) + (v1[1] ** 2) + (v1[2] ** 2))
        p4f = sqrt((v2[0] ** 2) + (v2[1] ** 2) + (v2[2] ** 2))
        denominador = (p3f * p4f)
        r_raiz = acos((p2f) / (denominador))
        angulo = p1f * r_raiz
        print(f"El producto escalar de los vectores es de: {round(angulo,2)}")
        print("""
        +-----------------------------------------------+
        |MENÚ                                           |
        |1) Introducir el primer vector                 |
        |2) Introducir el segundo vector                |   
        |3) Calcular la suma                            |    
        |4) Calcular la diferencia                      |
        |5) Calcular el producto escalar                |
        |6) Calcular el producto vectorial              |
        |7) Calcular el angulo (en grados) entre ellos  |
        |8) Calcular la longitud                        |
        |9) Finaliza                                    |
        +-----------------------------------------------+
        """)
        opcion = int(input("Ingresa la opcion a elegir: "))
    elif opcion == 8: 
        print("""     
        +---------------------------------------+
        |1) Longitud del Primer Vector          |
        |2) Longitud del Segundo Vector         |
        |3) Salir                               |
        +---------------------------------------+    
        """)
        s_opcion = int(input("¿Que operación quieres realizar? "))
        if s_opcion == 1: 
            vectorUnoL = sqrt(v1[0] ** 2 + v1[1] ** 2 + v1[2] ** 2)
            print(f"Lo longitud del Vector 1 es de {round(vectorUnoL,2)}")
            print("""
            +-----------------------------------------------+
            |MENÚ                                           |
            |1) Introducir el primer vector                 |
            |2) Introducir el segundo vector                |   
            |3) Calcular la suma                            |    
            |4) Calcular la diferencia                      |
            |5) Calcular el producto escalar                |
            |6) Calcular el producto vectorial              |
            |7) Calcular el angulo (en grados) entre ellos  |
            |8) Calcular la longitud                        |
            |9) Finaliza                                    |
            +-----------------------------------------------+
            """)
            opcion = int(input("Ingresa la opcion a elegir: "))
        if s_opcion == 2: 
            vectorUnoL = sqrt(v2[0] ** 2 + v2[1] ** 2 + v2[2] ** 2)
            print(f"Lo longitud del Vector 1 es de {round(vectorUnoL, 2)}")
            print("""
            +-----------------------------------------------+
            |MENÚ                                           |
            |1) Introducir el primer vector                 |
            |2) Introducir el segundo vector                |   
            |3) Calcular la suma                            |    
            |4) Calcular la diferencia                      |
            |5) Calcular el producto escalar                |
            |6) Calcular el producto vectorial              |
            |7) Calcular el angulo (en grados) entre ellos  |
            |8) Calcular la longitud                        |
            |9) Finaliza                                    |
            +-----------------------------------------------+
            """)
            opcion = int(input("Ingresa la opcion a elegir: "))
        elif s_opcion == 3: 
            break
        else: 
            print("Opcion no reconocida")
    elif opcion == 9: 
        break
else: 
    exit()