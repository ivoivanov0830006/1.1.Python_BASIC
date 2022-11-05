actors_name = input()
academy_points = float(input())
judges_count = int(input())
needed_points = 1250.5
total_points = academy_points
is_nominated = False

for judge in range(1, judges_count + 1):
    judge_name = input()
    judge_points = float(input())
    current_points = len(judge_name) * judge_points / 2
    total_points += current_points
    if total_points > 1250.5:
        is_nominated = True
        break

diff = abs(total_points - needed_points)
if is_nominated:
    print(f"Congratulations, {actors_name} got a nominee for leading role with {total_points:.1f}!")
else:
    print(f"Sorry, {actors_name} you need {diff:.1f} more!")
