budget = float(input())
ticket = input()
people = int(input())
price = 0
transport = 0

if ticket == "VIP":
    price = 499.99
    if 1 <= people <= 4:
        transport = budget * 0.75
    elif 5 <= people <= 9:
        transport = budget * 0.60
    elif 10 <= people <= 24:
        transport = budget * 0.50
    elif 25 <= people <= 49:
        transport = budget * 0.40
    elif people > 50:
        transport = budget * 0.25
elif ticket == "Normal":
    price = 249.99
    if 1 <= people <= 4:
        transport = budget * 0.75
    elif 5 <= people <= 9:
        transport = budget * 0.60
    elif 10 <= people <= 24:
        transport = budget * 0.50
    elif 25 <= people <= 49:
        transport = budget * 0.40
    elif people > 50:
        transport = budget * 0.25
total = transport + (price * people)
rest = abs(budget - total)
if budget >= total:
    print(f"Yes! You have {rest:.2f} leva left.")
else:
    print(f"Not enough money! You need {rest:.2f} leva.")
