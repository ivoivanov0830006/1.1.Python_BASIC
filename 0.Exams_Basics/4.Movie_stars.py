budget = float(input())
command = input()
total_expenses = 0
rest_budget = budget
is_not_enough = False

while command != "ACTION":
    actor_name = command
    if len(actor_name) > 15:
        salary = 0.2 * rest_budget
    else:
        salary = float(input())
    rest_budget -= salary
    total_expenses += salary
    if total_expenses > budget:
        is_not_enough = True
        break
    command = input()

diff = abs(total_expenses - budget)
if is_not_enough:
    print(f"We need {diff:.2f} leva for our actors.")
else:
    print(f"We are left with {diff:.2f} leva.")
