hrisantemas = int(input())
roses = int(input())
tulips = int(input())
season = input()
holiday = input()

price_h = 0
price_r = 0
price_t = 0

if season == "Spring" or season == "Summer":
    price_h = 2
    price_r = 4.1
    price_t = 2.5
elif season == "Autumn" or season == "Winter":
    price_h = 3.75
    price_r = 4.5
    price_t = 4.15
total = hrisantemas * price_h + roses * price_r + tulips * price_t
if holiday == "Y":
    total = total * 1.15
    if tulips > 7 and season == "Spring":
        total = total * 0.95
    elif roses >= 10 and season == "Winter":
        total = total * 0.9
elif holiday == "N":
    if tulips > 7 and season == "Spring":
        total = total * 0.95
    elif roses >= 10 and season == "Winter":
        total = total * 0.9
if (hrisantemas + roses + tulips) > 20:
    total = total * 0.8 + 2
else:
    total = total + 2
print(f"{total:.2f}")
