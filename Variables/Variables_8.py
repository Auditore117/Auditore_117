suma = 0

for i in range(5):
    numero = float(input(f"Ingrese el número {i + 1}: "))
    suma += numero

promedio = suma / 5

print(f"\nEl promedio es: {promedio:.2f}")