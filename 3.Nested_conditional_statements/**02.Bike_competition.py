juniors = int(input())
seniors = int(input())
trace = input()
price_j = 0
price_s = 0
if trace == "trail":
    price_j = 5.5
    price_s = 7
elif trace == "cross-country":
    if (juniors + seniors) >= 50:
        price_j = 8 * 0.75
        price_s = 9.5 * 0.75
    else:
        price_j = 8
        price_s = 9.5
elif trace == "downhill":
    price_j = 12.25
    price_s = 13.75
elif trace == "road":
    price_j = 20
    price_s = 21.5
total = (juniors * price_j) + (seniors * price_s)
expenses = total * 0.05
charity = total - expenses
print(f"{charity:.2f}")


