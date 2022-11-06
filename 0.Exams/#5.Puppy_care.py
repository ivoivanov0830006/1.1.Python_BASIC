food_amount_kg = int(input())
food_amount_g = food_amount_kg * 1000
command = input()
total_food = 0
is_enough = False

while command != "Adopted":
    current_food = int(command)
    total_food += current_food
    command = input()

if total_food <= food_amount_g:
    is_enough = True
diff = abs(total_food - food_amount_g)

if is_enough:
    print(f"Food is enough! Leftovers: {diff} grams.")
else:
    print(f"Food is not enough. You need {diff} grams more.")
