print("")
numero = int(input("Ingrese un número entero para mostrar su tabla de multiplicar: "))
print("")

print(f"\nTabla de multiplicar de {numero}:")
print("")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
    print("")