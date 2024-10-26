print("")
cuenta = float(input("Ingrese el monto de la cuenta: $"))
print("")

if cuenta < 150000:
    metodo_pago = "pago en efectivo"
    print(f"\nPara una cuenta de ${cuenta:.2f}, se recomienda: {metodo_pago}.")
    print("")
elif 150000 <= cuenta <= 300000:
    metodo_pago = "pago con el celular (dinero electrónico)"
    print(f"\nPara una cuenta de ${cuenta:.2f}, se recomienda: {metodo_pago}.")
    print("")
elif 300000 < cuenta <= 600000:
    metodo_pago = "pago con tarjeta de débito"
    print(f"\nPara una cuenta de ${cuenta:.2f}, se recomienda: {metodo_pago}.")
    print("")
else:
    metodo_pago = "pago con tarjeta de crédito"
    print(f"\nPara una cuenta de ${cuenta:.2f}, se recomienda: {metodo_pago}.")
print("")
