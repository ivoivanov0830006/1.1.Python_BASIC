budget = int(input())
season = input()
count = int(input())
price = 0

if season == "Spring":
    price = 3000
elif season == "Summer":
    price = 4200
elif season == "Autumn":
    price = 4200
elif season == "Winter":
    price = 2600

if count <= 6:
    price = price * 0.9
elif 7 <= count <= 11:
    price = price * 0.85
elif count >= 12:
    price = price * 0.75

if count % 2 == 0 and season != "Autumn":
    price = price * 0.95

rest = abs(budget - price)
if budget >= price:
    print(f"Yes! You have {rest:.2f} leva left.")
else:
    print(f"Not enough money! You need {rest:.2f} leva.")
