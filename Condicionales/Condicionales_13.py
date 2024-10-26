print("")
peso = float(input("Ingrese el peso en kg: "))
print("")
estatura = float(input("Ingrese la estatura en metros: "))
print("")

imc = peso / (estatura * estatura)

if imc < 18.5:
    estado = "Bajo peso"
    print(f"\nEl IMC calculado es: {imc:.2f}")
    print("")
    print(f"Estado: {estado}")
    print("")
elif 18.5 <= imc < 24.9:
    estado = "Normal"
    print(f"\nEl IMC calculado es: {imc:.2f}")
    print("")
    print(f"Estado: {estado}")
    print("")
elif 25 <= imc < 29.9:
    estado = "Sobrepeso"
    print(f"\nEl IMC calculado es: {imc:.2f}")
    print("")
    print(f"Estado: {estado}")
    print("")
elif 30 <= imc < 34.9:
    estado = "Obesidad 1"
    print(f"\nEl IMC calculado es: {imc:.2f}")
    print("")
    print(f"Estado: {estado}")
    print("")
elif 35 <= imc < 39.9:
    estado = "Obesidad 2"
    print(f"\nEl IMC calculado es: {imc:.2f}")
    print("")
    print(f"Estado: {estado}")
    print("")
elif 40 <= imc < 49.9:
    estado = "Obesidad 3"
    print(f"\nEl IMC calculado es: {imc:.2f}")
    print("")
    print(f"Estado: {estado}")
    print("")
else:
    estado = "Obesidad 4"
    print(f"\nEl IMC calculado es: {imc:.2f}")
    print("")
    print(f"Estado: {estado}")
    print("")