flowers = input()
count = int(input())
budget = int(input())
price = 0

if flowers == "Roses":
    price = 5
    if count > 80:
        price = price * 0.9
elif flowers == "Dahlias":
    price = 3.8
    if count > 90:
        price = price * 0.85
elif flowers == "Tulips":
    price = 2.8
    if count > 80:
        price = price * 0.85
elif flowers == "Narcissus":
    price = 3
    if count < 120:
        price = price * 1.15
elif flowers == "Gladiolus":
    price = 2.5
    if count < 80:
        price = price * 1.2
        
total = price * count
rest = abs(budget - total)

if budget >= total:
    print(f"Hey, you have a great garden with {count} {flowers} and {rest:.2f} leva left.")
else:
    print(f"Not enough money, you need {rest:.2f} leva more.")
