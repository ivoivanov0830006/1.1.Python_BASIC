num = (float(input()))
number = int(100 * num)
total = 0

while number != 0:
    if number >= 200:
        number -= 200
    elif number >= 100:
        number -= 100
    elif number >= 50:
        number -= 50
    elif number >= 20:
        number -= 20
    elif number >= 10:
        number -= 10
    elif number >= 5:
        number -= 5
    elif number >= 2:
        number -= 2
    elif number >= 1:
        number -= 1
    total += 1
print(f"{total}")
