city = input()
package = input()
vip = input()
days = int(input())

price = 0

if days > 7:
    days = days - 1
if city not in ("Bansko", "Borovets", "Varna", "Burgas"):
    print("Invalid input!")
elif package not in ("noEquipment", "withEquipment", "noBreakfast", "withBreakfast"):
    print("Invalid input!")
elif days < 1:
    print("Days must be positive number!")
else:
    if city == "Bansko" or city == "Borovets":
        if package == "noEquipment":
            price = 80
            if vip == "yes":
                price = price * 0.95
        elif package == "withEquipment":
            price = 100
            if vip == "yes":
                price = price * 0.9
    elif city == "Varna" or city == "Burgas":
        if package == "noBreakfast":
            price = 100
            if vip == "yes":
                price = price * 0.93
        elif package == "withBreakfast":
            price = 130
            if vip == "yes":
                price = price * 0.88
    total = price * days
    print(f"The price is {total:.2f}lv! Have a nice time!")
