budget = float(input())
season = input()
type_holiday = ""
destination = ""
total = 0

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        type_holiday = "Camp"
        total = budget * 0.3
    elif season == "winter":
        type_holiday = "Hotel"
        total = budget * 0.7
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        type_holiday = "Camp"
        total = budget * 0.4
    elif season == "winter":
        type_holiday = "Hotel"
        total = budget * 0.8
elif budget > 1000:
    destination = "Europe"
    type_holiday = "Hotel"
    total = budget * 0.9

print(f"Somewhere in {destination}")
print(f"{type_holiday} - {total:.2f}")
