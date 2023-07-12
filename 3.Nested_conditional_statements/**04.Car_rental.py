budget = float(input())
season = input()

car_class = ""
car_type = ""
price = 0

if budget <= 100:
    car_class = "Economy class"
    if season == "Summer":
        car_type = "Cabrio"
        price = budget * 0.35
    elif season == "Winter":
        price = budget * 0.65
        car_type = "Jeep"
elif 100 < budget <= 500:
    car_class = "Compact class"
    if season == "Summer":
        car_type = "Cabrio"
        price = budget * 0.45
    elif season == "Winter":
        price = budget * 0.80
        car_type = "Jeep"
else:
    car_class = "Luxury class"
    price = budget * 0.9
    car_type = "Jeep"
print(f"{car_class}")
print(f"{car_type} - {price:.2f}")
