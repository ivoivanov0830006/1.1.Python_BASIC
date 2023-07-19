days = int(input())
type_room = input()
experience = input()

nights = days - 1
price = 0

if nights < 10:
    if type_room == "room for one person":
        price = 18
    elif type_room == "apartment":
        price = 25 * 0.7
    elif type_room == "president apartment":
        price = 35 * 0.9
elif 10 <= nights <= 15:
    if type_room == "room for one person":
        price = 18
    elif type_room == "apartment":
        price = 25 * 0.65
    elif type_room == "president apartment":
        price = 35 * 0.85
elif nights > 15:
    if type_room == "room for one person":
        price = 18
    elif type_room == "apartment":
        price = 25 * 0.5
    elif type_room == "president apartment":
        price = 35 * 0.8

total = price * nights

if experience == "positive":
    total = total * 1.25
elif experience == "negative":
    total = total * 0.9
print(f"{total:.2f}")
