suma = 0

for i in range(10):
    print("")
    numero = float(input(f"Ingrese el número {i + 1}: "))
    print("")
    suma += numero

promedio = suma / 10
print(f"\nLa suma de los números es: {suma:.2f}")
print("")
print(f"El promedio de los números es: {promedio:.2f}")
print("")