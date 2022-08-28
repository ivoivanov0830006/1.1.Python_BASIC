needed_money = float(input())
current_money = float(input())

days = 0
spend_in_row = 0

while current_money < needed_money:
    text = input()
    money = float(input())
    days += 1
    last_action = text
    if text == "spend":
        current_money -= money
        if last_action == "spend":
            spend_in_row += 1
            if spend_in_row == 5:
                break
        if current_money < 0:
            current_money = 0
    elif text == "save":
        current_money += money
if current_money >= needed_money:
    print(f"You saved the money for {days} days.")
if spend_in_row == 5:
    print("You can't save the money.")
    print(f"{days}")
