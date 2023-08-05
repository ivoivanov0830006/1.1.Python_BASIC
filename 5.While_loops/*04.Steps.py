goal_steps = 10000
otherinput = input()
total_steps = 0

while otherinput != "Going home":
    current_steps = int(otherinput)
    total_steps += current_steps
    if total_steps > 10000:
        break
    otherinput = input()
if otherinput == "Going home":
    home_steps = int(input())
    total_steps += home_steps
diff = abs(total_steps - goal_steps)
if total_steps >= goal_steps:
    print(f"Goal reached! Good job!")
    print(f"{diff} steps over the goal!")
elif total_steps < goal_steps:
    print(f"{diff} more steps to reach goal.")

# ------------------------------------- Problem to resolve ------------------------------
#
# Габи иска да започне здравословен начин на живот и си е поставила за цел да върви 10 000 стъпки всеки ден.
# Някои дни обаче е много уморена от работа и ще иска да се прибере преди да постигне целта си. Напишете
# програма, която чете от конзолата по колко стъпки изминава тя всеки път като излиза през деня и когато
# постигне целта си да се изписва "Goal reached! Good job!" и колко стъпки повече е извървяла
# "{разликата между стъпките} steps over the goal!"
# Ако иска да се прибере преди това, тя ще въведе командата "Going home" и ще въведе стъпките, които е
# извървяла докато се прибира. След което, ако не е успяла да постигне целта си, на конзолата трябва да
# се изпише: "{разликата между стъпките} more steps to reach goal."
# Вход	                    Изход
# 1000                      Goal reached! Good job!
# 1500                      1000 steps over the goal!
# 2000
# 6500
# ---------------------------------------------------------
# 1500                      2500 more steps to reach goal.
# 300
# 2500
# 3000
# Going home
# 200
# ---------------------------------------------------------
# 1500                      Goal reached! Good job!
# 3000                      298 steps over the goal!
# 250
# 1548
# 2000
# Going home
# 2000
