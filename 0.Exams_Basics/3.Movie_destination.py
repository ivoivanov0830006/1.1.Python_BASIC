budget = float(input())
destination = input()
season = input()
days = int(input())
price = 0
discount = 1

if season == "Winter":
    if destination == "Dubai":
        price = 45000
        discount = 0.7
    elif destination == "Sofia":
        price = 17000
        discount = 1.25
    elif destination == "London":
        price = 24000
elif season == "Summer":
    if destination == "Dubai":
        price = 40000
        discount = 0.7
    elif destination == "Sofia":
        price = 12500
        discount = 1.25
    elif destination == "London":
        price = 20250

total_price = price * days * discount
diff = abs(total_price - budget)
if total_price <= budget:
    print(f"The budget for the movie is enough! We have {diff:.2f} leva left!")
else:
    print(f"The director needs {diff:.2f} leva more!")
