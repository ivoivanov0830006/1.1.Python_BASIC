num1 = 1
num2 = 1
total = 0

while num1 <= 10:
    num2 = 1
    while num2 <= 10:
        total = num1 * num2
        print(f"{num1} * {num2} = {total}")
        num2 += 1
    num1 += 1

------------ANOTHER SOLUTION-------------------

# for num1 in range (1, 11):
#     for num2 in range (1, 11):
#         total = num1 * num2
#         print(f"{num1} * {num2} = {total}")
