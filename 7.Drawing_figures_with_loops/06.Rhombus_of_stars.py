
n = int(input())

#Top Rows + Middle Row
for row in range(1, n + 1):
    for col in range(1, n - row + 1):
        print(" ", end="")
    print("*", end="")

    for col in range(1, row):
        print(" *", end="")
    print()

#Bottom Rows
for row in range(1, n):
    for col in range(1, row + 1):
        print(" ", end="")
    print("*", end="")

    for col in range(1, n - row):
        print(" *", end="")
    print()
