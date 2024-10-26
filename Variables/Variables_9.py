valor_unitario = float(input("Ingrese el valor unitario del producto: "))
cantidad = int(input("Ingrese la cantidad de productos comprados: "))

subtotal = valor_unitario * cantidad
iva = subtotal * 0.16
total = subtotal + iva

print(f"\nEl valor total a pagar es: ${total:.2f}")