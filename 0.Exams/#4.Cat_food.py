cat_count = int(input())
food_price_kg = 12.45
food_price_g = food_price_kg / 1000
total_small_cats = 0
total_big_cats = 0
total_huge_cats = 0
total_food = 0

for cat in range(1, cat_count + 1):
    food_amount = int(input())
    if 100 <= food_amount < 200:
        total_small_cats += 1
    elif 200 <= food_amount < 300:
        total_big_cats += 1
    elif 300 <= food_amount < 400:
        total_huge_cats += 1
    total_food += food_amount

total_price = total_food * food_price_g

print(f"Group 1: {total_small_cats} cats.")
print(f"Group 2: {total_big_cats} cats.")
print(f"Group 3: {total_huge_cats} cats.")
print(f"Price for food per day: {total_price:.2f} lv.")
