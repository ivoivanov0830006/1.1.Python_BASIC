total_days = int(input())
total_hours = int(input())
total_sum = 0

for day in range(1, total_days + 1):
    total = 0
    for hour in range (1, total_hours + 1):
        if day % 2 == 0 and hour % 2 != 0:
            price = 2.5
        elif day % 2 != 0 and hour % 2 == 0:
            price = 1.25
        else:
            price = 1
        total += price
    print(f"Day: {day} - {total:.2f} leva")
    total_sum += total
print(f"Total: {total_sum:.2f} leva")
