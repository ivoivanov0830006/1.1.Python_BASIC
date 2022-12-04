budget = float(input())
budget_left = budget
item_count = 0
total_sum = 0

command = input()

while command != "Stop":
    price = float(input())
    item_count += 1
    if item_count % 3 == 0:
        price = price * 0.5
    if price > budget_left:
        diff = abs(price - budget_left)
        print("You don't have enough money!")
        print(f"You need {diff:.2f} leva!")
        break
    budget_left -= price
    total_sum += price
    command = input()
if command == "Stop":
    print(f"You bought {item_count} products for {total_sum:.2f} leva.")
