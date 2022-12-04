eggs_size = input()
eggs_color = input()
number_batches = int(input())
total_sum = 0
batch_price = 0

if eggs_size == "Large":
    if eggs_color == "Red":
        batch_price = 16
    elif eggs_color == "Green":
        batch_price = 12
    elif eggs_color == "Yellow":
        batch_price = 9
elif eggs_size == "Medium":
    if eggs_color == "Red":
        batch_price = 13
    elif eggs_color == "Green":
        batch_price = 9
    elif eggs_color == "Yellow":
        batch_price = 7
elif eggs_size == "Small":
    if eggs_color == "Red":
        batch_price = 9
    elif eggs_color == "Green":
        batch_price = 8
    elif eggs_color == "Yellow":
        batch_price = 5
total_sum = number_batches * batch_price
total_sum *= 0.65
print(f"{total_sum:.2f} leva.")
