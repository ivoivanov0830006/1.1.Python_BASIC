total_finish_bottles = int(input())
total_finish = total_finish_bottles * 750
command = input()
washing_count = 0
dishes_count = 0
pots_count = 0
needed_finish = 0
current_finish = 0
is_ended = False
is_empty = False

while command != "End":
    current_item = int(command)
    washing_count += 1
    if command == "End":
        is_ended = True
        break
    elif washing_count % 3 == 0:
        pots_count += current_item
        current_finish = current_item * 15
    else:
        dishes_count += current_item
        current_finish = current_item * 5
    needed_finish += current_finish
    if needed_finish > total_finish:
        is_empty = True
        break
    command = input()
needed_finish = dishes_count * 5 + pots_count * 15
diff = abs(needed_finish - total_finish)
if is_ended or is_empty:
    print(f"Not enough detergent, {diff} ml. more necessary!")
if needed_finish <= total_finish:
    print(f"Detergent was enough!")
    print(f"{dishes_count} dishes and {pots_count} pots were washed.")
    print(f"Leftover detergent {diff} ml.")

#Гошо работи в ресторант и отговаря за зареждането на съдомиялната накрая на деня.
#Вашата задача е да напишете програма, която изчислява, дали дадено закупено количество бутилки от препарат 
#за съдомиялна е достатъчно, за да измие определено количество съдове. Знае се, че всяка бутилка съдържа 
#750 мл. препарат, за 1 чиния са нужни 5 мл., а за тенджера 15 мл.  Приемете, че на всяко трето зареждане със съдове, 
#съдомиялната се пълни само с тенджери, а останалите пъти с чинии. Докато не получите команда "End" ще продължите 
#да получавате бройка съдове, които трябва да бъдат измити.
#Вход
#От конзолата се четат:
#Брой бутилки от препарат, който ще бъде използван за миенето на чинии - цяло число в интервала [1…10] 
#На всеки следващ ред, до получаване на командата "End" или докато количеството препарат не се изчерпи, 
#брой съдове, които трябва да бъдат измити - цяло число в интервала [1…100]
#Изход
#В случай, че количеството препарат е било достатъчно за измиването на съдовете:
#"Detergent was enough!"
#"{брой чисти чинии} dishes and {брой чисти тенджери} pots were washed."
#"Leftover detergent {количество останал препарат} ml."
#В случай, че количеството препарат не е било достатъчно за измиването на съдовете:
#"Not enough detergent, {количество не достигнал препарат} ml. more necessary!"
#Вход                           Изход
#2                              Detergent was enough!
#53                             118 dishes and 55 pots were washed.
#65                             Leftover detergent 85 ml.
#55
#End
#----------------------------------------------------------------------
#1                              Not enough detergent, 100 ml. more necessary!
#10
#15
#10
#12
#13
#30
