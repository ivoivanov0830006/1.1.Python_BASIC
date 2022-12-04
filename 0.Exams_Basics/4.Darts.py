starting_points = 301
current_points = starting_points
total_success_shots = 0
total_fail_shots = 0
name = input()
command = input()
is_winning = False
is_retired = False

while command != "Retire":
    section = command
    points = int(input())
    if section == "Single":
        points = points
    elif section == "Double":
        points = points * 2
    elif section == "Triple":
        points = points * 3
    total_success_shots += 1
    previous_points = current_points
    current_points -= points
    if current_points == 0:
        is_winning = True
        break
    elif current_points < 0:
        current_points = previous_points
        total_fail_shots += 1
        total_success_shots -= 1
    command = input()
    if command == "Retire":
        is_retired = True
if is_winning:
    print(f"{name} won the leg with {total_success_shots} shots.")
if is_retired:
    print(f"{name} retired after {total_fail_shots} unsuccessful shots.")
