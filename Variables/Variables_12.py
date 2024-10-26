import math

cateto_a = float(input("Ingrese la longitud del primer cateto: "))
cateto_b = float(input("Ingrese la longitud del segundo cateto: "))

hipotenusa = math.sqrt(cateto_a ** 2 + cateto_b ** 2)

print(f"\nLa hipotenusa es: {hipotenusa:.2f}")