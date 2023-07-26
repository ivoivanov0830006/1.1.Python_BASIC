import sys
n = int(input())
max_number = -sys.maxsize
total = 0
for number in range(1, n + 1):
    current_number = int(input())
    total = total + current_number
    if current_number > max_number:
        max_number = current_number
if total / 2 == max_number:
    print("Yes")
    print(f"Sum = {max_number}")
else:
    diff = abs(max_number - (total - max_number))
    print("No")
    print(f"Diff = {diff}")
    
# Да се напише програма, която чете n-на брой цели числа, въведени от потребителя,и проверява дали сред тях
# съществува число, което е равно на сумата на всички останали.
# ⦁	Ако има такъв елемент печата "Yes" и на нов ред "Sum = "  + неговата стойност
# ⦁	Ако няма такъв елемент печата "No" и на нов ред "Diff = " + разликата между най-големия елемент и
# умата на останалите (по абсолютна стойност)
# вход	                    изход
# 7                         Yes
# 3                         Sum = 12
# 4
# 1
# 1
# 2
# 12
# 1	
# -------------------------------------------
# 4                         Yes
# 6                         Sum = 6
# 1
# 2
# 3	
# --------------------------------------------
# 3                         No
# 1                         Diff = 8
# 1 
# 10
