voucher_value = int(input())
command = input()
total_tickets = 0
total_items = 0

while command != "End":
    current_item = command
    if len(current_item) > 8:
        price = ord(current_item[0]) + ord(current_item[1])
        voucher_value -= price
        if voucher_value < 0:
            break
        total_tickets += 1
    elif len(current_item) <= 8:
        price = ord(current_item[0])
        voucher_value -= price
        if voucher_value < 0:
            break
        total_items += 1
    command = input()
print(f"{total_tickets}")
print(f"{total_items}")
