holiday = float(input())
count_puzzle = int(input())
count_doll = int(input())
count_bear = int(input())
count_minion = int(input())
count_truck = int(input())
price_puzzle = 2.6
price_doll = 3
price_bear = 4.1
price_minion = 8.2
price_truck = 2
rest = 0
needed = 0
total = 0
total_earn = price_puzzle * count_puzzle + price_doll * count_doll + \
             price_bear * count_bear + price_minion * count_minion + \
             price_truck * count_truck
total_count = count_puzzle + count_doll + count_bear + count_minion + count_truck
if total_count >= 50:
    total = total_earn - (0.25 * total_earn)
    rent = 0.1 * total
    total = total - rent
    if total >= holiday:
        rest = total - holiday
        print(f"Yes! {rest:.2f} lv left.")
    else:
        needed = holiday - total
        print(f"Not enough money! {needed:.2f} lv needed.")
elif total_count < 50:
    total = total_earn
    rent = 0.1 * total
    total = total_earn - rent
    if total >= holiday:
        rest = total - holiday
        print(f"Yes! {rest:.2f} lv left.")
    else:
        needed = holiday - total
        print(f"Not enough money! {needed:.2f} lv needed.")
