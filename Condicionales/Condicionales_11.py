print("")
print("Seleccione el tamaño de la pizza:")
print("")
print("1. Tamaño 1 - $15,000")
print("")
print("2. Tamaño 2 - $24,000")
print("")
print("3. Tamaño 3 - $36,000")
print("")
tamaño = int(input("Ingrese el número del tamaño de pizza que desea: "))
print("")

if tamaño == 1:
    precio_base = 15000
    print(f"\nEl precio base por la pizza de tamaño {tamaño} es: ${precio_base}.")
    print("")
elif tamaño == 2:
    precio_base = 24000
    print(f"\nEl precio base por la pizza de tamaño {tamaño} es: ${precio_base}.")
    print("")
elif tamaño == 3:
    precio_base = 36000
    print(f"\nEl precio base por la pizza de tamaño {tamaño} es: ${precio_base}.")
    print("")
else:
    print("Tamaño inválido.")
    print("")

if precio_base is not None:
    num_ingredientes = int(input("Ingrese el número de ingredientes adicionales: "))
    print("")
    costo_ingredientes = num_ingredientes * 4000
    precio_total = precio_base + costo_ingredientes
    print(f"\nEl precio total a pagar por la pizza es: ${precio_total:.2f}.")
print("")