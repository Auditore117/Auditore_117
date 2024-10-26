print("")
print("Ingrese 3 números")
print("")

num1 = float(input("Ingrese el primer número: "))
print("")
num2 = float(input("Ingrese el segundo número: "))
print("")
num3 = float(input("Ingrese el tercer número: "))
print("")

numeros = [num1, num2, num3]

numeros_ascendente = sorted(numeros)

numeros_descendente = sorted(numeros, reverse=True)

print("\nNúmeros en orden ascendente:", numeros_ascendente)
print("")
print("Números en orden descendente:", numeros_descendente)
print("")