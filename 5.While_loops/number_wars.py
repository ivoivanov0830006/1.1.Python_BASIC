player_1_name = input()
player_2_name = input()
command = input()
is_number_wars = False
is_end_of_game = False


player_1_points = 0
player_2_points = 0
winning_points = 0
winner = ()


while command != "End of game":
    player_1_card = int(command)
    player_2_card = int(input())
    if player_1_card > player_2_card:
        player_1_points += player_1_card - player_2_card
    elif player_1_card < player_2_card:
        player_2_points += player_2_card - player_1_card
    else:
        is_number_wars = True
        player_1_card = int(input())
        player_2_card = int(input())
        if player_1_card > player_2_card:
            winner = player_1_name
            winning_points = player_1_points
        elif player_1_card < player_2_card:
            winner = player_2_name
            winning_points = player_2_points
        break
    command = input()
    if command == "End of game":
        is_end_of_game = True
        break
if is_end_of_game:
    print(f"{player_1_name} has {player_1_points} points")
    print(f"{player_2_name} has {player_2_points} points")
if is_number_wars:
    print("Number wars!")
    print(f"{winner} is winner with {winning_points} points")


#"Numbers" е нова игра, която се играе с 36 карти (двойки, тройки, четворки, петици, шестици, седмици, осмици, деветки и десетки от всички 4 бои). Правилата на играта са следните:
#Играе се от двама играчи, които започват с равен брой карти
#На всяко раздаване всеки един от тях дава по 1 карта:
#Ако картата на първия играч е с по-голяма стойност от картата на втория играч, първият получава точки, които са равни на разликата между картата на първия и картата на втория (например: първият дава тройка купа, а вторият двойка каро -> първият печели, защото 3 > 2 и точките, които печели, са 3 – 2 = 1).
#Ако картата на втория играч е с по-голяма стойност от картата на първия играч, вторият получава точки, които са равни на разликата между картата на втория и картата на първия (например: вторият дава осмица пика, а първият шестица спатия -> вторият печели, защото 8 > 6 и точките, които печели, са 8 – 6 = 2).
#Ако картите, които дават двамата, са с еднаква стойност, тогава се получава "Number wars" и всеки един от играчите трябва да даде по още една карта. Играчът, чиято карта е с по-голяма стойност, печели и играта приключва(В този случай, няма да има еднакви карти).
#Освен при "Number wars", играта може да приключи и при команда "End of game". Тогава никой не печели и играта приключва.
#Вход
#Първоначално се четат два реда:
#Име на първия играч - текст
#Име на втория играч - текст
#След това, до получаване на команда "End of game", се четат многократно по два реда:
#Карта, която дава първият играч- цяло число в интервала [2…9]
#Карта, която дава вторият играч -  цяло число в интервала [2…9]
#При еднакви карти на двамата играчи се прочитат нови два реда (карта, която дава първият и карта, която дава вторият.) 
#Изход
#При случая, в който има "Number wars ", да се отпечата:
#"Number wars!"
#"{име на победителя} is winner with {брой натрупани точки} points"
#При команда "End of game" да се отпечатат два реда:
#"{име на първия играч} has {брой натрупани точки за първия играч} points"
#"{име на втория играч} has {брой натрупани точки за втория играч} points"
#Вход                          Изход
#Desi                          Number wars!
#Niki                          Desi is winner with 2 points
#7
#5
#3
#4
#3
#3
#5
#3
