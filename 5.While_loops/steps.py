goal_steps = 10000
otherinput = input()
total_steps = 0

while otherinput != "Going home":
    current_steps = int(otherinput)
    total_steps += current_steps
    if total_steps > 10000:
        break
    otherinput = input()
if otherinput == "Going home":
    home_steps = int(input())
    total_steps += home_steps
diff = abs(total_steps - goal_steps)
if total_steps >= goal_steps:
    print(f"Goal reached! Good job!")
    print(f"{diff} steps over the goal!")
elif total_steps < goal_steps:
    print(f"{diff} more steps to reach goal.")
