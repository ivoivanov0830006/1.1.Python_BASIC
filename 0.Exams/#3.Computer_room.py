month = input()
hours_count = int(input())
people_count = int(input())
day_time = input()
price = 0

if month == "march" or month == "april" or month == "may":
    if day_time == "day":
        price = 10.5
    elif day_time == "night":
        price = 8.4
elif month == "june" or month == "july" or month == "august":
    if day_time == "day":
        price = 12.6
    elif day_time == "night":
        price = 10.2
if people_count >= 4:
    price = price * 0.9
if hours_count >= 5:
    price = price * 0.5

total_price = price * hours_count * people_count

print(f"Price per person for one hour: {price:.2f}")
print(f"Total cost of the visit: {total_price:.2f}")
