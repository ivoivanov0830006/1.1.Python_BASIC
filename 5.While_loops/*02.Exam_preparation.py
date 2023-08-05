needed_fails = int(input())
name = input()
fails = 0
total_score = 0
total_tasks = 0
is_failed = False
last_name = ""

while name != "Enough":
    current_score = int(input())
    total_score += current_score
    total_tasks += 1
    last_name = name
    if current_score <= 4:
        fails += 1
        if fails == needed_fails:
            is_failed = True
            break
    name = input()
if is_failed:
    print(f"You need a break, {fails} poor grades.")
else:
    average_score = total_score / total_tasks
    print(f"Average score: {average_score:.2f}")
    print(f"Number of problems: {total_tasks}")
    print(f"Last problem: {last_name}")
