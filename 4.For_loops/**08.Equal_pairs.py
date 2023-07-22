pairs = int(input())
diff = 0
maxdiff = 0
previous_sum = 0
current_sum = 0

for number in range(1, pairs * 2 + 1):
    current_num = int(input())
    current_sum += current_num
    if number % 2 == 0 and number != 2:
        diff = abs(current_sum - previous_sum)
        if diff > maxdiff:
            maxdiff = diff
        previous_sum = current_sum
        current_sum = 0
    elif number == 2:
        previous_sum = current_sum
        current_sum = 0
if maxdiff == 0:
    print(f"Yes, value={previous_sum}")
else:
    print(f"No, maxdiff={maxdiff}")
