print("")
edad = int(input("Ingrese su edad: "))
print("")
genero = int(input("Ingrese su género (1 para femenino, 2 para masculino): "))
print("")

if genero == 1:  
    pulsaciones = (220 - edad) / 10
    print(f"\nNúmero de pulsaciones para una mujer de {edad} años: {pulsaciones:.2f} pulsaciones cada 10 segundos.")
    print("")
elif genero == 2:  # Masculino
    pulsaciones = (210 - edad) / 10
    print(f"\nNúmero de pulsaciones para un hombre de {edad} años: {pulsaciones:.2f} pulsaciones cada 10 segundos.")
    print("")
else:
    print("Género inválido")
    print("")