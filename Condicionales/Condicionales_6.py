import math

print("")
print("escoja el número acorde a la figura de la que desea saber el area")
print("")
print(" 1 para rectángulo")
print("")
print(" 2 para cuadrado")
print("")
print(" 3 para paralelogramo")
print("")
print(" 4 para rombo")
print("")
print(" 5 para trapecio")
print("")
print(" 6 para triángulo")
print("")
print(" 7 para triángulo equilátero")
print("")
print(" 8 para triángulo rectángulo")
print("")
print(" 9 para polígono regular")
print("")
num = int(input(""))
print("")

if num == 1:
    base = float(input("Ingrese la base del rectángulo: "))
    altura = float(input("Ingrese la altura del rectángulo: "))
    area = base * altura
    print("El área del rectángulo es: ", area)
elif num == 2:
    lado = float(input("Ingrese el lado del cuadrado: "))
    area = lado * lado
    print("El área del cuadrado es: ", area)
elif num == 3:
    base = float(input("Ingrese la base del paralelogramo: "))
    altura = float(input("Ingrese la altura del paralelogramo: "))
    area = base * altura
    print("El área del paralelogramo es: ", area)
elif num == 4:
    diagonal1 = float(input("Ingrese la longitud de la diagonal 1: "))
    diagonal2 = float(input("Ingrese la longitud de la diagonal 2: "))
    area = (diagonal1 * diagonal2) / 2
    print("El área del rombo es: ", area)
elif num == 5:
    base = float(input("Ingrese la base del trapecio: "))
    altura = float(input("Ingrese la altura del trapecio: "))
    base2 = float(input("Ingrese la base inferior del trapecio: "))
    area = ((base + base2) * altura) / 2
    print("El área del trapecio es: ", area)
elif num == 6:
    base = float(input("Ingrese la base del triángulo: "))
    altura = float(input("Ingrese la altura del triángulo: "))
    area = (base * altura) / 2
    print("El área del triángulo es: ", area)
elif num == 7:
    lado = float(input("Ingrese el lado del triángulo equilátero: "))
    area = (lado * lado) / 2
    print("El área del triángulo equilátero es: ", area)
elif num == 8:
    base = float(input("Ingrese la base del triángulo rectángulo: "))
    altura = float(input("Ingrese la altura del triángulo rectángulo: "))
    area = (base * altura) / 2
    print("El área del triángulo rectángulo es: ", area)
elif num == 9:
    lados = int(input("Ingrese el número de lados del polígono regular: "))
    lado = float(input("Ingrese la longitud de cada lado: "))
    area = (lados * lado * lado) / (6 * (math.sqrt(3)))
    print("El área del polígono regular es: ", area)
else:
    print("Opción inválida")