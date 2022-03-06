print("""
 Diseña un algoritmo que calcule el IVA (16%) de un producto dado su precio de venta sin IVA.
""")
precio_venta = float(input("Precio del producto (sin IVA): "))
IVA_porcentaje = precio_venta * 0.16
print(f"Debe pagar un IVA con el monto de ${IVA_porcentaje}")
IVA_total = precio_venta + IVA_porcentaje
print("El monto a pagar ya con IVA es de: ", IVA_total)