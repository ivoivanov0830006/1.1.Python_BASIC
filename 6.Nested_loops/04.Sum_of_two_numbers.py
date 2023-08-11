start_interval = int(input())
end_interval = int(input())
magic_number = int(input())
current_combination = 0
is_found = False

for first_number in range(start_interval, end_interval + 1):
    for second_number in range(start_interval, end_interval + 1):
        current_combination += 1
        total_combinations = current_combination
        if first_number + second_number == magic_number:
            is_found = True
            break
    if is_found:
        break
        
if is_found:
    print(f"Combination N:{current_combination} ({first_number} + {second_number} = {magic_number})")
else:
    print(f"{total_combinations} combinations - neither equals {magic_number}")



#Напишете програма която проверява всички възможни комбинации от двойка числа в интервала от две дадени числа. 
#На изхода се отпечатва, коя поред е комбинацията чиито сбор от числата е равен на дадено магическо число. 
#Ако няма нито една комбинация отговаряща на условието се печата съобщение, че не е намерено.
#Вход
#Входът се чете от конзолата и се състои от три реда:
#Първи ред – начало на интервала – цяло число в интервала [1...999]
#Втори ред – край на интервала – цяло число в интервала [по-голямо от първото число...1000]
#Трети ред – магическото число – цяло число в интервала [1...10000]
#Изход
#На конзолата трябва да се отпечата един ред, според резултата:
#Ако е намерена комбинация чиито сбор на числата е равен на магическото число
#"Combination N:{пореден номер} ({първото число} + {второ число} = {магическото число})"
#Ако не е намерена комбинация отговаряща на условието
#"{броят на всички комбинации} combinations - neither equals {магическото число}"
#Вход                     Изход
#1                        Combination N:4 (1 + 4 = 5)
#10
#5
#------------------------------------------------------
#23                       4 combinations - neither equals 20
#24
#20
