turns = int(input())

points = 0
total_numbers_10 = 0
total_numbers_20 = 0
total_numbers_30 = 0
total_numbers_40 = 0
total_numbers_50 = 0
invalid = 0

for turn in range(1, turns + 1):
    number = int(input())
    if 0 <= number <= 9:
        points += 0.2 * number
        total_numbers_10 += 1
    elif 10 <= number <= 19:
        points += + 0.3 * number
        total_numbers_20 += 1
    elif 20 <= number <= 29:
        points += + 0.4 * number
        total_numbers_30 += 1
    elif 30 <= number <= 39:
        points += 50
        total_numbers_40 += 1
    elif 40 <= number <= 50:
        points += 100
        total_numbers_50 += 1
    else:
        points /= 2
        invalid += 1
total_numbers = total_numbers_10 + total_numbers_20 + total_numbers_30 + total_numbers_40 + total_numbers_50 + invalid
percent_10 = total_numbers_10 / total_numbers * 100
percent_20 = total_numbers_20 / total_numbers * 100
percent_30 = total_numbers_30 / total_numbers * 100
percent_40 = total_numbers_40 / total_numbers * 100
percent_50 = total_numbers_50 / total_numbers * 100
percent_invalid = invalid / total_numbers * 100

print(f"{points:.2f}")
print(f"From 0 to 9: {percent_10:.2f}%")
print(f"From 10 to 19: {percent_20:.2f}%")
print(f"From 20 to 29: {percent_30:.2f}%")
print(f"From 30 to 39: {percent_40:.2f}%")
print(f"From 40 to 50: {percent_50:.2f}%")
print(f"Invalid numbers: {percent_invalid:.2f}%")
