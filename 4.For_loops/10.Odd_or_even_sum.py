n = int(input())

odd_sum = 0
even_sum = 0

for number in range(1, n + 1):
    current_num = int(input())
    if number % 2 == 0:
        even_sum = even_sum + current_num
    else:
        odd_sum = odd_sum + current_num
        
if even_sum == odd_sum:
    print(f"Yes")
    print(f"Sum = {even_sum}")
else:
    diff = abs(odd_sum - even_sum)
    print(f"No")
    print(f"Diff = {diff}")
    
    
#Да се напише програма, която чете n-на брой цели числа, 
#подадени от потребителя и проверява дали сумата от числата на 
#четни позиции е равна на сумата на числата на нечетни позиции. 
#⦁	Ако сумите са равни да се отпечатат два реда: 
#         "Yes" и на нов ред "Sum = " + сумата; 
#⦁	Ако сумите не са равни да се отпечат два реда: 
#         "No" и на нов ред "Diff = " + разликата. 
#Разликата се изчислява по абсолютна стойност. 
#вход             изход
#4                Yes
#10               Sum = 70
#50
#60
#20
#------------------------------------------
#4                No
#3                Diff = 1
#5
#1
#-2
