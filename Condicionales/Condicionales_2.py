print("")
nombre = input("Ingrese su nombre: ")
print("")
edad = int(input("Ingrese su edad: "))
print("")

if edad >= 18 and edad <= 100:
    print("Usted es mayor de edad")
    print("")
elif edad > 100:
    print("Edad incorrecta")
    print("")
elif edad < 0:
    print("Edad incorrecta")
else:
    print("Usted es menor de edad")
    print("")
print("Fin del programa")
print("")