command = input()
win_count = 0
lose_count = 0

while command != "End of tournaments":
    if command == "End of tournaments":
        break
    name = command
    games_count = int(input())
    for game_number in range(1, games_count + 1):
        points_ally = int(input())
        points_enemy = int(input())
        diff = abs(points_enemy - points_ally)
        if points_ally > points_enemy:
            win_count += 1
            print(f"Game {game_number} of tournament {name}: win with {diff} points.")
        else:
            lose_count += 1
            print(f"Game {game_number} of tournament {name}: lost with {diff} points.")
    command = input()

total_matches = win_count + lose_count
total_win_percentage = win_count / total_matches * 100
total_lose_percentage = lose_count / total_matches * 100
print(f"{total_win_percentage:.2f}% matches win")
print(f"{total_lose_percentage:.2f}% matches lost")
