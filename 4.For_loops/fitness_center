guest_count = int(input())
total_shake = 0
total_bar = 0
total_legs = 0
total_back = 0
total_chest = 0
total_abs = 0
total = 0

for person in range(1, guest_count + 1):
    activity = input()
    if activity == "Protein bar":
        total_bar += 1
        total += 1
    elif activity == "Protein shake":
        total_shake += 1
        total += 1
    elif activity == "Legs":
        total_legs += 1
        total += 1
    elif activity == "Back":
        total_back += 1
        total += 1
    elif activity == "Chest":
        total_chest += 1
        total += 1
    elif activity == "Abs":
        total_abs += 1
        total += 1

total_train = total_abs + total_back + total_chest + total_legs
total_protein = total_shake + total_bar

percentage_train = total_train / total * 100
percentage_protein = total_protein / total * 100

print(f"{total_back} - back")
print(f"{total_chest} - chest")
print(f"{total_legs} - legs")
print(f"{total_abs} - abs")
print(f"{total_shake} - protein shake")
print(f"{total_bar} - protein bar")
print(f"{percentage_train:.2f}% - work out")
print(f"{percentage_protein:.2f}% - protein")

#Напишете програма, която да изчислява броя на посетителите в един фитнес център. 
#В началото програмата получава броя на посетителите на фитнеса и за всеки човек - 
#дейността, която извършва във фитнеса. На края програмата трябва да отпечата броят 
#трениращи за всяка една дейност ("Back", "Chest", 'Legs", "Abs") и броят клиенти, 
#закупили продукт ("Protein shake", "Protein bar"). Също така - процентът трениращи 
#(спрямо общия брой посетители) и процентът на клиентите, закупили продукт от фитнеса.
#Вход
#От конзолата се чете число, след това поредица от низове, всяко на отделен ред:
#На първия ред – броят на посетителите във фитнеса – цяло число в интервала [1...1000]
#За всеки един посетител на отделен ред – дейността във фитнеса – текст ("Back", "Chest", "Legs",
#"Abs", "Protein shake" или "Protein bar")
#Изход
#Да се отпечатат на конзолата 8 реда, които съдържат следната информация:
#"{брой хора трениращи гръб} - back"
#"{брой хора трениращи гърди} - chest"
#"{брой хора трениращи крака} - legs"
#"{брой хора трениращи коремни мускули} - abs"
#"{брой хора закупили протеинов шейк} - protein shake"
#"{брой хора закупили протеинов блок} - protein bar"
#"{процент на хората дошли да тренират}% - work out"
#"{процент на хората дошли да купят протеин}% - protein"
#Всички проценти трябва да са форматирани до втората цифра след десетичния знак.
#Вход                     Изход
#10                       1 - back
#Back                     1 - chest
#Chest                    2 - legs
#Legs                     2 - abs
#Abs                      2 - protein shake
#Protein shake            2 - protein bar   
#Protein bar              60.00% - work out
#Protein shake            40.00% - protein
#Protein bar
#Legs
#Abs
