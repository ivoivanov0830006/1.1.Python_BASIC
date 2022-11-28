from math import ceil
name = input()
budget = float(input())
beer_count = int(input())
beer_price = 1.2
chips_count = int(input())

beer_total = beer_price * beer_count
chips_total = ceil(0.45 * beer_total * chips_count)

total_sum = beer_total + chips_total
diff = abs(total_sum - budget)

if total_sum <= budget:
    print(f"{name} bought a snack and has {diff:.2f} leva left.")
else:
    print(f"{name} needs {diff:.2f} more leva!")
