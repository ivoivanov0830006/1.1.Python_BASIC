import math
wine_area_m2 = int(input())
grape_m2 = float(input())
needed_wine_liters = int(input())
workers = int(input())

total_grape = wine_area_m2 * grape_m2
total_wine = (0.4 * total_grape) / 2.5
rest = 0

if total_wine >= needed_wine_liters:
    rest = math.ceil(total_wine - needed_wine_liters)
    rest_per_worker = math.ceil(rest / workers)
    print(f"Good harvest this year! Total wine: {math.floor(total_wine)} liters.")
    print(f"{rest} liters left -> {rest_per_worker} liters per person.")
else:
    rest = math.floor(abs(total_wine - needed_wine_liters))
    print(f"It will be a tough winter! More {rest} liters wine needed.")
