team_name = input()
games_count = int(input())
total_wins = 0
total_draws = 0
total_loses = 0
total_points = 0

for game in range(1, games_count + 1):
    result = input()
    if result == "W":
        total_wins += 1
        total_points += 3
    elif result == "D":
        total_draws += 1
        total_points += 1
    elif result == "L":
        total_loses += 1

if games_count == 0:
    print(f"{team_name} hasn't played any games during this season.")
else:
    win_percentage = total_wins / games_count * 100
    print(f"{team_name} has won {total_points} points during this season.")
    print("Total stats:")
    print(f"## W: {total_wins}")
    print(f"## D: {total_draws}")
    print(f"## L: {total_loses}")
    print(f"Win rate: {win_percentage:.2f}%")
