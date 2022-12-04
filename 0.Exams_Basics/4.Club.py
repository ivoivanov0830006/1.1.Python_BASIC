needed_money = float(input())
command = input()
total_money = 0
is_successful = False

while command != "Party!":
    cocktail_name = command
    cocktail_count = int(input())
    price = len(cocktail_name)
    current_total = price * cocktail_count
    if current_total % 2 != 0:
        current_total = 0.75 * current_total
    total_money += current_total
    if total_money >= needed_money:
        is_successful = True
        break
    command = input()
diff = abs(total_money - needed_money)
if is_successful:
    print("Target acquired.")
else:
    print(f"We need {diff:.2f} leva more.")
print(f"Club income - {total_money:.2f} leva.")
