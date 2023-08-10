total_number = int(input())
total = 0

while total != total_number:
    number = int(input())
    total += number
    if total >= total_number:
        break
print(f"{total}")
