total_months = int(input())

total_electricity = 0
total_water = 0
total_internet = 0
total_other = 0

for month in range(1, total_months + 1):
    electricity = float(input())
    total_electricity += electricity
    total_water += 20
    total_internet += 15
total_other = (total_electricity + total_water + total_internet) * 1.2
average = (total_electricity + total_water + total_internet + total_other) / total_months

print(f"Electricity: {total_electricity:.2f} lv")
print(f"Water: {total_water:.2f} lv")
print(f"Internet: {total_internet:.2f} lv")
print(f"Other: {total_other:.2f} lv")
print(f"Average: {average:.2f} lv")
