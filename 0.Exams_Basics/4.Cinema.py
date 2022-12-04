total_seats = int(input())
command = input()
total_people = 0
is_full = False
price = 5
current_bill = 0
total_money = 0

while command != "Movie time!":
    current_people = int(command)
    total_people += current_people
    current_bill = current_people * price
    if current_people % 3 == 0:
        current_bill -= 5
    if total_people > total_seats:
        is_full = True
        break
    total_money += current_bill
    current_bill = 0
    command = input()
if is_full:
    print("The cinema is full.")
else:
    diff = total_seats - total_people
    print(f"There are {diff} seats left in the cinema.")
print(f"Cinema income - {total_money} lv.")
