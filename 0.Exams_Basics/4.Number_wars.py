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
