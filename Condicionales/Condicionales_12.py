print("")
cantidad = int(input("Ingrese la cantidad de artículos: "))
print("")
precio_unitario_original = float(input("Ingrese el precio unitario original: $"))
print("")

if cantidad <= 5:
    descuento = 0
    precio_total = cantidad * precio_unitario_original
    print(f"\nEl valor total a pagar por {cantidad} artículos es: ${precio_total:.2f}.")
    print("")
elif 5 < cantidad < 10:
    descuento = 0.05  
    precio_total = cantidad * precio_unitario_original * (1 - descuento)
    print(f"\nEl valor total a pagar por {cantidad} artículos es: ${precio_total:.2f}.")
    print("")
else:
    descuento = 0.08 
    precio_total = cantidad * precio_unitario_original * (1 - descuento)
    print(f"\nEl valor total a pagar por {cantidad} artículos es: ${precio_total:.2f}.")
print("")