budget = float(input())
series_count = int(input())
total_cost = 0

for series in range(1, series_count + 1):
    series_name = input()
    series_price = float(input())
    if series_name == "Thrones":
        total_cost += series_price * 0.5
    elif series_name == "Lucifer":
        total_cost += series_price * 0.6
    elif series_name == "Protector":
        total_cost += series_price * 0.7
    elif series_name == "TotalDrama":
        total_cost += series_price * 0.8
    elif series_name == "Area":
        total_cost += series_price * 0.9
    else:
        total_cost += series_price

diff = abs(total_cost - budget)
if total_cost > budget:
    print(f"You need {diff:.2f} lv. more to buy the series!")
else:
    print(f"You bought all the series and left with {diff:.2f} lv.")
