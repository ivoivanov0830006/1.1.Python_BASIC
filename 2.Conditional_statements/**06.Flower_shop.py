import math
magnolia_count = int(input())
ziumbiul_count = int(input())
rose_count = int(input())
cactus_count = int(input())
gift_price = float(input())
magnolia = 3.25
ziumbiul = 4
rose = 3.5
cactus = 8
total = magnolia_count * magnolia + ziumbiul_count * ziumbiul + rose_count * rose + cactus_count * cactus
total_money = total * 0.95
if total_money >= gift_price:
    rest = math.floor(abs(total_money - gift_price))
    print(f"She is left with {rest} leva.")
else:
    rest = math.ceil(abs(total_money - gift_price))
    print(f"She will have to borrow {rest} leva.")
