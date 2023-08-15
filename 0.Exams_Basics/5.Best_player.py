command = input()
is_hat_trick_made = False
best_player = ""
most_goals = 0

while command != "END":
    player_name = command
    current_goals_count = int(input())
    if current_goals_count > most_goals:
        most_goals = current_goals_count
        best_player = player_name
    if current_goals_count >= 3:
        is_hat_trick_made = True
    if current_goals_count >= 10:
        break
    command = input()

print(f"{best_player} is the best player!")
if is_hat_trick_made:
    print(f"He has scored {most_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {most_goals} goals.")
