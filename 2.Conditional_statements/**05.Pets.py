import math
days_gone = int(input())
total_food = int(input())
dog_food = float(input())
cat_food = float(input())
turtle_food = float(input())

needed_food = (dog_food + cat_food + (turtle_food/1000)) * days_gone
food_left = 0

if total_food >= needed_food:
    food_left = math.floor(abs(total_food - needed_food))
    print(f"{food_left} kilos of food left.")
else:
    food_left = math.ceil(abs(total_food - needed_food))
    print(f"{food_left} more kilos of food are needed.")
