count = int(input())
total_numbers = 0
sum_numbers = 0

while total_numbers != count:
    current_number = int(input())
    sum_numbers += current_number
    total_numbers += 1
    if total_numbers == count:
        break
average = sum_numbers / count
print(f"{average:.2f}")
