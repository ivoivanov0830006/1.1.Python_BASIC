locations_count = int(input())

for location in range(1, locations_count + 1):
    total_income = 0
    expected_income_per_day = int(input())
    working_days = int(input())
    for days in range(1, working_days + 1):
        income = int(input())
        total_income += income
    average_total_income = total_income / working_days
    if average_total_income >= expected_income_per_day:
        print(f"Good job! Average gold per day: {average_total_income:.2f}.")
    else:
        diff = expected_income_per_day - average_total_income
        print(f"You need {diff:.2f} gold.")
