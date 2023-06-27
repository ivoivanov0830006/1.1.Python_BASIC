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

      
# --------------------------- Another Solution ----------------------------
#
# trip_price = float(input())
# puzzle_count = int(input())
# dolls_count = int(input())
# teddy_count = int(input())
# minions_count = int(input())
# trucks_count = int(input())
#
# total_sum = puzzle_count * 2.6 + dolls_count * 3 + teddy_count * 4.1 + minions_count * 8.2 + trucks_count * 2
# all_count = puzzle_count + dolls_count + teddy_count + minions_count + trucks_count
# if all_count >= 50:
#     total_sum = total_sum * 0.75
# total_sum = total_sum - (total_sum * 0.1)
# difference = abs(total_sum - trip_price)
# if total_sum >= trip_price:
#     print(f"Yes! {difference:.2f} lv left.")
# else:
#     print(f"Not enough money! {difference:.2f} lv needed")
