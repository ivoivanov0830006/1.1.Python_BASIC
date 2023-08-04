count = int(input())
total_numbers = 0
sum_numbers = 0

while total_numbers != count:
    current_number = int(input())
    sum_numbers += current_number
    total_numbers += 1
    if total_numbers == count:
        break
average = sum_numbers / count
print(f"{average:.2f}")

# Напишете програма, която прочита едно число n, след това прочита n на брой цели числа и принтира 
# средно аритметичното на тяхната сума число, форматирано до втората цифра след десетични знак.
# вход	                    изход
# 4                         2.75
# 3
# 2
# 4
# 2	
# ----------------------------------------
# 2                         5.00
# 6
# 4
# ----------------------------------------	 	
# 3                         49.00
# 82
# 43
# 22
# ----------------------------------------	 	
# 4                         54.25
# 95
# 23
# 76
# 23
