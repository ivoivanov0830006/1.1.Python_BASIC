beverage = input()
sugar = input()
count = int(input())
espresso_no_sugar = 0.9
cappuccino_no_sugar = 1
tea_no_sugar = 0.5
espresso = 1
cappuccino = 1.2
tea = 0.6
espresso_sugar = 1.2
cappuccino_sugar = 1.6
tea_sugar = 0.7
total = 0

if beverage == "Espresso":
    if sugar == "Without":
        total = 0.65 * (espresso_no_sugar * count)
        if count > 5:
            total = 0.75 * total
            if total > 15:
                total = 0.8 * total
    elif sugar == "Normal":
        total = espresso * count
        if count > 5:
            total = 0.75 * total
            if total > 15:
                total = 0.8 * total
    elif sugar == "Extra":
        total = espresso_sugar * count
        if count > 5:
            total = 0.75 * total
            if total > 15:
                total = 0.8 * total

elif beverage == "Cappuccino":
    if sugar == "Without":
        total = 0.65 * (cappuccino_no_sugar * count)
        if total > 15:
            total = 0.8 * total
    elif sugar == "Normal":
        total = cappuccino * count
        if total > 15:
            total = 0.8 * total
    elif sugar == "Extra":
        total = cappuccino_sugar * count
        if total > 15:
            total = 0.8 * total

elif beverage == "Tea":
    if sugar == "Without":
        total = 0.65 * (tea_no_sugar * count)
        if total > 15:
            total = 0.8 * total
    elif sugar == "Normal":
        total = tea * count
        if total > 15:
            total = 0.8 * total
    elif sugar == "Extra":
        total = tea_sugar * count
        if total > 15:
            total = 0.8 * total
print(f"You bought {count} cups of {beverage} for {total:.2f} lv.")
