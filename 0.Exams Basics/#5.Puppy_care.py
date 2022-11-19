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


# ------------------------------------- Problem to resolve ------------------------------
#
# Ани намира кученце, за което ще се грижи, докато се намери някой да го осинови. То изяжда дневно 
# определено количество храна. Да се напише програма, която проверява дали количеството храна, което 
# е закупено за кученцето, ще е достатъчно докато кученцето бъде осиновено.
# Вход:
# От конзолата се прочитат:
# Закупеното количество храна за кученцето в килограми – цяло число в интервала [1 …100]
# На всеки следващ ред до получаване на команда Adopted ще получавате колко грама изяжда кученцето 
# на всяко хранене - цяло число в интервала [10 …1000]
# Изход:
# На конзолата се отпечатва 1 ред:
# Ако количеството храна е достатъчно да се отпечата:
#  	"Food is enough! Leftovers: {останала храна} grams." 
# Ако количеството храна не е достатъчно да се отпечата:
#  	"Food is not enough. You need {нужно количество храна} grams more." 
# -------------------------------------- Example inputs ----------------------------------
# Вход	                Изход	
# 4                     Food is enough! Leftovers: 2595 grams.
# 130
# 345
# 400
# 180
# 230
# 120
# Adopted
# ---------------------------------------------------------------------------------------
# 3                     Food is enough! Leftovers: 0 grams.
# 1000
# 1000
# 1000
# Adopted
# ----------------------------------------------------------------------------------------
# 2                     Food is not enough. You need 2032 grams more.
# 999
# 456
# 999
# 999
# 123
# 456
# Adopted
