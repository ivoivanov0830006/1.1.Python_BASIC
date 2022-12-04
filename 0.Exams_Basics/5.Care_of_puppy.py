food_in_kg = int(input())
food_in_g = food_in_kg * 1000
command = input()

while command != "Adopted":
    eaten_food_in_g = int(command)
    food_in_g -= eaten_food_in_g
    command = input()
if food_in_g < 0:
    print(f"Food is not enough. You need {abs(food_in_g)} grams more.")
else:
    print(f"Food is enough! Leftovers: {food_in_g} grams.")
