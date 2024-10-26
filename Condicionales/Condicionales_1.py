print("")
numero = int(input("Ingrese un número: "))
print("")

if numero % 2 == 0 and numero > 0:
    print(f"{numero} es un número par")
    print("")
elif numero % 2 == 1 and numero > 0:
    print(f"{numero} es un número impar")
    print("")
elif numero < 0:
    print(f"{numero} no es un número Natural")
    print("")
else:
    print("El número ingresado es cero")
    print("")
