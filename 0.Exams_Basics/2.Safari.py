budget = float(input())
liters = float(input())
day = input()


fuel_per_liter = 2.1
tour_guy = 100
discount_percentage = 0

if day == "Saturday":
    discount_percentage = 10

elif day == "Sunday":
    discount_percentage = 20

total_cost = (tour_guy + fuel_per_liter * liters) * ((100 - discount_percentage) / 100)
diff = abs(total_cost - budget)

if budget >= total_cost:
    print(f"Safari time! Money left: {diff:.2f} lv.")
else:
    print(f"Not enough money! Money needed: {diff:.2f} lv.")
