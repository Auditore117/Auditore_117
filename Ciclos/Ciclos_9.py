print("")
n = int(input("Ingrese un número entero para calcular su factorial: "))
print("")
factorial = 1

for i in range(1, n + 1):
    factorial *= i

print(f"El factorial de {n} es: {factorial}")
print("")