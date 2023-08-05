needed_money = float(input())
current_money = float(input())

days = 0
spend_in_row = 0

while current_money < needed_money:
    text = input()
    money = float(input())
    days += 1
    last_action = text
    if text == "spend":
        current_money -= money
        if last_action == "spend":
            spend_in_row += 1
            if spend_in_row == 5:
                break
        if current_money < 0:
            current_money = 0
    elif text == "save":
        current_money += money
if current_money >= needed_money:
    print(f"You saved the money for {days} days.")
if spend_in_row == 5:
    print("You can't save the money.")
    print(f"{days}")

# -----------------ANOTHER_SOLUTION--------------------

# needed_money = float(input())
# current_money = float(input())

# days = 0
# spend_in_row = 0

# while current_money < needed_money:
#     text = input()
#     money = float(input())
#     days += 1

#     if text == "spend":
#         current_money -= money
#         spend_in_row += 1
#         if spend_in_row == 5:
#             break
#         if current_money < 0:
#             current_money = 0
#     elif text == "save":
#         current_money += money
#         spend_in_row = 0

# if current_money >= needed_money:
#     print(f"You saved the money for {days} days.")
# if spend_in_row == 5:
#     print("You can't save the money.")
#     print(f"{days}")

# Джеси е решила да събира пари за екскурзия и иска от вас да ѝ помогнете да разбере дали ще успее да 
# събере необходимата сума. Тя спестява или харчи част от парите си всеки ден. Ако иска да похарчи 
# повече от наличните си пари, то тя ще похарчи колкото има и ще ѝ останат 0 лева.
# Вход
# От конзолата се четат:
# ⦁	Пари, нужни за екскурзията - реално число;
# ⦁	Налични пари - реално число.
# След това многократно се четат по два реда:
# ⦁	Вид действие – текст с две възможности: "spend" или "save";
# ⦁	Сумата, която ще спести/похарчи - реално число.
# Изход
# Програмата трябва да приключи при следните случаи:
# ⦁	Ако 5 последователни дни Джеси само харчи, на конзолата да се изпише:
# ⦁	"You can't save the money."
# ⦁	"{Общ брой изминали дни}"
# ⦁	Ако Джеси събере парите за почивката, на конзолата се изписва:
# ⦁	"You saved the money for {общ брой изминали дни} days."
# Вход	                                    Изход
# 2000                                      You saved the money for 2 days.
# 1000
# spend
# 1200
# save
# 2000	
# ---------------------------------------------------------------
# 110                                       You can't save the money.
# 60                                        5	
# spend
# 10
# spend
# 10
# spend
# 10
# spend
# 10
# spend
# 10	
# ---------------------------------------------------------------
# 250                                       You saved the money for 4 days.	
# 150
# spend
# 50
# spend
# 50
# save
# 100
# save
# 100	
