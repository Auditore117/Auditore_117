print("")
n = int(input("Ingrese el número de términos de la serie de Fibonacci que desea mostrar: "))
print("")
a, b = 0, 1
suma = 0

print("Serie de Fibonacci:")
print("")
for _ in range(n):
    print(a, end=" ")
    suma += a
    a, b = b, a + b
print(f"\nLa suma de los primeros {n} términos es: {suma}")
print("")