n = int(input())

#Top Row
print("+", end="")
for i in range(n - 2):
    print(" -", end="")
print(" +")
#Middle Rows
for row in range(n - 2):
    print("|", end="")
    for col in range(n - 2):
        print(" -", end="")
    print(" |")
#Bottom Row
print("+", end="")
for i in range(n - 2):
    print(" -", end="")
print(" +")
