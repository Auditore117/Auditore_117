print("")
numero_llantas = int(input("Ingrese el número de llantas compradas: "))
print("")

if numero_llantas < 6:
    precio_unitario = 240000
    print(f"\nEl precio unitario por llantas es: ${precio_unitario}.")
    print("")
elif 6 <= numero_llantas <= 7:
    precio_unitario = 221000
    print(f"\nEl precio unitario por llantas es: ${precio_unitario}.")
    print("")
else:
    precio_unitario = 180000
    print(f"\nEl precio unitario por llantas es: ${precio_unitario}.")
    print("")

valor_total = numero_llantas * precio_unitario
print(f"\nEl valor total a pagar por {numero_llantas} llantas es: ${valor_total:.2f}.")
print("")
