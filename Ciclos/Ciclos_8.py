n = 4
numero = 1

for i in range(1, n + 1):
    print("")
    print(' ' * (n - i) + ' '.join(str(numero + j) for j in range(i)))
    print("")
    numero += i