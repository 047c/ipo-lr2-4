import math

x = int(input("Введите число x: "))
y = int(input("Введите число y: "))
psi = (math.fabs((x**(y/x)) - ((y/x)** (1. / 3.))) + (y-x))
print(f"Значение функции: {psi}")