import sys
n = int(input())
odd_max = -sys.maxsize
odd_min = sys.maxsize
even_max = -sys.maxsize
even_min = sys.maxsize
odd_sum = 0
even_sum = 0

for number in range(1, n + 1):
    current_number = float(input())
    if number % 2 != 0:
        odd_sum += current_number
        if current_number < odd_min:
            odd_min = current_number
        if current_number > odd_max:
            odd_max = current_number
    else:
        even_sum += current_number
        if current_number < even_min:
            even_min = current_number
        if current_number > even_max:
            even_max = current_number
print(f"OddSum={odd_sum:.2f},")
if odd_min == sys.maxsize:
    print("OddMin=No,")
else:
    print(f"OddMin={odd_min:.2f},")
if odd_max == -sys.maxsize:
    print("OddMax=No,")
else:
    print(f"OddMax={odd_max:.2f},")
print(f"EvenSum={even_sum:.2f},")
if even_min == sys.maxsize:
    print("EvenMin=No,")
else:
    print(f"EvenMin={even_min:.2f},")
if even_max == -sys.maxsize:
    print("EvenMax=No")
else:
    print(f"EvenMax={even_max:.2f}")
    
    
#Напишете програма, която чете n-на брой числа, въведени от потребителя, 
#и пресмята сумата, минимума и максимума на числата на четни и нечетни позиции (броим от 1). 
#Когато няма минимален / максимален елемент, отпечатайте "No". 
#Изходът да се форматира в следния вид:
#"OddSum=" + {сума на числата на нечетни позиции},
#"OddMin=" + { минимална стойност на числата на нечетни позиции } / {“No”},
#"OddMax=" + { максимална стойност на числата на нечетни позиции } / {“No”},
#"EvenSum=" + { сума на числата на четни позиции },
#"EvenMin=" + { минимална стойност на числата на четни позиции } / {“No”},
#"EvenMax=" + { максимална стойност на числата на четни позиции } / {“No”}
#Всяко число трябва да е форматирано до втория знак след десетичната запетая.
#вход                     изход
#6                        OddSum=9.00, 
#2                        OddMin=2.00, 
#3                        OddMax=5.00, 
#5                        EvenSum=8.00, 
#4                        EvenMin=1.00, 
#2                        EvenMax=4.00
#1
------------------------------------------
#1                        OddSum=-5.00,
#-5	                      OddMin=-5.00, 
#                         OddMax=-5.00, 
#                         EvenSum=0.00, 
#                         EvenMin=No, 
#                         EvenMax=No
