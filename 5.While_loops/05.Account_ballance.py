otherinput = input()
total = 0

while otherinput != "NoMoreMoney":
    deposit = float(otherinput)
    if deposit < 0:
        print("Invalid operation!")
        break
    total += deposit
    print(f"Increase: {deposit:.2f}")
    otherinput = input()
print(f"Total: {total:.2f}")

total_sum = 0
command = input()

# while direction != "NoMoreMoney":
#     current_sum = float(direction)
#     if current_sum < 0:
#         print("Invalid operation!")
#         break
#     print(f"Increase: {current_sum:.2f}")
#     total_sum += current_sum
#     direction = input()
# print(f"Total: {total_sum:.2f}")

