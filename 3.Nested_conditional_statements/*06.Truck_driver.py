season = input()
distance_per_month = float(input())

price = 0

if distance_per_month <= 5000:
    if season == "Spring" or season == "Autumn":
        price = 0.75
    elif season == "Summer":
        price = 0.9
    elif season == "Winter":
        price = 1.05
elif 5000 < distance_per_month <= 10000:
    if season == "Spring" or season == "Autumn":
        price = 0.95
    elif season == "Summer":
        price = 1.1
    elif season == "Winter":
        price = 1.25
elif 10000 < distance_per_month <= 20000:
    price = 1.45
total = (distance_per_month * price * 4) * 0.9
print(f"{total:.2f}")
