number = int(input())

current = 1
is_bigger_than_n = False
for row in range(1, number + 1):
    for column in range(1, row + 1):
        if current > number:
            break
        print(current, end=" ")
        current += 1
    if is_bigger_than_n:
        break
    print()
