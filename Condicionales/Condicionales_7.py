print("")
print("escoja el número acorde a la temperatura de la que desea hacer la conversion")
print("")
print(" 1 Fahrenheit")
print("")
print(" 2 Celsius")
print("")
print(" 3 Kelvin")
print("")
print(" 4 Rankine")
print("")
print(" 5 Réaumur")
print("")
num = int(input(""))
print("")

if num == 1:
    fahrenheit = float(input("Ingrese la temperatura en Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    kelvin = celsius + 273.15
    rankine = fahrenheit + 459.67
    reaumur = celsius * 4/5
    print(f"{fahrenheit} °F es igual a {celsius:.2f} °C, {kelvin:.2f} K, {rankine:.2f} °R, {reaumur:.2f} °Re")
elif num == 2:
    celsius = float(input("Ingrese la temperatura en Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    kelvin = celsius + 273.15
    rankine = (celsius + 273.15) * 9/5
    reaumur = celsius * 4/5
    print(f"{celsius} °C es igual a {fahrenheit:.2f} °F, {kelvin:.2f} K, {rankine:.2f} °R, {reaumur:.2f} °Re")
elif num == 3:
    kelvin = float(input("Ingrese la temperatura en Kelvin: "))
    celsius = kelvin - 273.15
    fahrenheit = (celsius * 9/5) + 32
    rankine = kelvin * 9/5
    reaumur = celsius * 4/5
    print(f"{kelvin} K es igual a {celsius:.2f} °C, {fahrenheit:.2f} °F, {rankine:.2f} °R, {reaumur:.2f} °Re")
elif num == 4:
    rankine = float(input("Ingrese la temperatura en Rankine: "))
    kelvin = rankine * 5/9
    celsius = kelvin - 273.15
    fahrenheit = (celsius * 9/5) + 32
    reaumur = celsius * 4/5
    print(f"{rankine} °R es igual a {kelvin:.2f} K, {celsius:.2f} °C, {fahrenheit:.2f} °F, {reaumur:.2f} °Re")
elif num == 5:
    reaumur = float(input("Ingrese la temperatura en Réaumur: "))
    celsius = reaumur * 5/4
    fahrenheit = (celsius * 9/5) + 32
    kelvin = celsius + 273.15
    rankine = (celsius + 273.15) * 9/5
    print(f"{reaumur} °Re es igual a {celsius:.2f} °C, {fahrenheit:.2f} °F, {kelvin:.2f} K, {rankine:.2f} °R")
else:
    print("Opción invalida")