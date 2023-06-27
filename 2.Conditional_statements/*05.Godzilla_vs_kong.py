budget = float(input())
stat = int(input())
clothes = float(input())
total_clothes = stat * clothes
decor = 0.1 * budget
rest = 0
needed = 0
if stat >= 150:
    total_clothes = total_clothes - 0.1 * total_clothes
    expense = decor + total_clothes
    if budget < expense:
        needed = expense - budget
        print(f"Not enough money!")
        print(f"Wingard needs {needed:.2f} leva more.")
    elif budget >= expense:
        rest = budget - expense
        print(f"Action!")
        print(f"Wingard starts filming with {rest:.2f} leva left.")
elif stat < 150:
    expense = decor + total_clothes
    if budget < expense:
        needed = expense - budget
        print(f"Not enough money!")
        print(f"Wingard needs {needed:.2f} leva more.")
    elif budget >= expense:
        rest = budget - expense
        print(f"Action!")
        print(f"Wingard starts filming with {rest:.2f} leva left.")
