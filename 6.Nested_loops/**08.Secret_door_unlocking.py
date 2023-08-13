x1 = int(input())
x2 = int(input())
x3 = int(input())

for i in range(2, x1 + 1, 2):
    for j in range(2, x2 + 1):
        for k in range(2, x3 + 1, 2):
            if j == 2 or j == 3 or j == 5 or j == 7:
                print(f"{i} {j} {k}")
