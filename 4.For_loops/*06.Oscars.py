actor_name = input()
points = float(input())
jury_count = int(input())

rest = 0
total_points = points

for jury in range(1, jury_count + 1):
    jury_name = input()
    jury_points = float(input())
    total_points = total_points + (len(jury_name) * jury_points) / 2
    if total_points > 1250.5:
        break
if total_points <= 1250.5:
    rest = 1250.5 - total_points
    print(f"Sorry, {actor_name} you need {rest:.1f} more!")
else:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!")
