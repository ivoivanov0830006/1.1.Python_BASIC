length = int(input())
width = int(input())
command = input()

total_pieces = 0
all_pieces = length * width
is_finished = False

while command != "STOP":
    current_pieces = int(command)
    total_pieces += current_pieces
    if total_pieces >= all_pieces:
        is_finished = True
        break
    command = input()
diff = abs(total_pieces - all_pieces)
if is_finished:
    print(f"No more cake left! You need {diff} pieces more.")
else:
    print(f"{diff} pieces are left.")

    
# ------------------------------------- Problem to resolve ------------------------------
#
# Поканени сте на 30-ти рожден ден, на който рожденикът черпи с огромна торта. Той обаче не знае 
# колко парчета могат да си вземат гостите от нея. Вашата задача е да напишете програма, която 
# изчислява броя на парчетата, които гостите са взели преди тя да свърши. Ще получите размерите 
# на тортата (широчина и дължина – цели числа и след това на всеки ред, до получаване на командата 
# "STOP" или докато не свърши тортата, броят на парчетата, които гостите вземат от нея. Всяко парче 
# торта е с размер 1х1 см.
# Да се отпечата на конзолата един от следните редове:
# ⦁	"{брой парчета} pieces are left." - ако стигнете до STOP и не са свършили парчетата торта;
# ⦁	"No more cake left! You need {брой недостигащи парчета} pieces more."
# Вход	                Изход	
# 10                    No more cake left! You need 1 pieces more.	
# 10
# 20
# 20
# 20
# 20
# 21	
# ------------------------------------------------------
# 10                    8 pieces are left.
# 2
# 2
# 4
# 6
# STOP
