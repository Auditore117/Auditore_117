n = 5

for i in range(1, n + 1):
    print("")
    print(' ' * (n - i) + '*' * i)
    print("")

for i in range(n - 1, 0, -1):
    print(' ' * (n - i) + '*' * i)
    print("")