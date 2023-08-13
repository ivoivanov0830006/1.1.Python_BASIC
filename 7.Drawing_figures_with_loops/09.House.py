import math
n = int(input())

stars = 1
if n % 2 == 0:
    stars += 1

roof_length = math.ceil(n / 2)

for i in range(0, roof_length):
    not_roof = (n - stars) // 2
    print(" " * not_roof + "*" * stars + " " * not_roof)
    stars += 2

for j in range(0, n // 2):
    print("|" + "*" * (n - 2) + "|")
