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


# ------------------------------ Another Solution ----------------------------
#
# budget = float(input())
# count_stat = int(input())
# price_cloth = float(input())
# decor = budget * 0.1
# all_clothes_price = count_stat * price_cloth
# if count_stat > 150:
#     all_clothes_price = all_clothes_price * 0.9
# expenses = decor + all_clothes_price
# diff = abs(expenses - budget)
# if expenses <= budget:
#     print("Action!")
#     print(f"Wingard starts filming with {diff:.2f} leva left.")
# else:
#     print("Not enough money!")
#     print(f"Wingard needs {diff:.2f} leva more.")
