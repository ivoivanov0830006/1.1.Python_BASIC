n = int(input())
total_2 = 0
total_3 = 0
total_4 = 0

for number in range(1, n + 1):
    current_number = int(input())
    if current_number % 2 == 0:
        total_2 += 1
    if current_number % 3 == 0:
        total_3 += 1
    if current_number % 4 == 0:
        total_4 += 1
percentage_2 = total_2 / n * 100
percentage_3 = total_3 / n * 100
percentage_4 = total_4 / n * 100
print(f"{percentage_2:.2f}%")
print(f"{percentage_3:.2f}%")
print(f"{percentage_4:.2f}%")
