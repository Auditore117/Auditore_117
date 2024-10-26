n = 7 
print("")
print(' ' * (n // 2) + '*' * n)
print("")
for i in range(1, n - 1):
    print(' ' * (n - i - 1) + '*')
    print("")

print(' ' * (n // 2) + '*' * n)
print("")