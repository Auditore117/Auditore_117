segundos = int(input("Ingrese el tiempo en segundos: "))

horas = segundos // 3600
minutos = (segundos % 3600) // 60

print(f"\nEl tiempo es: {horas} horas y {minutos} minutos.")