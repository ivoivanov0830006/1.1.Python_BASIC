import sys
n = int(input())
max_number = -sys.maxsize
total = 0
for number in range(1, n + 1):
    current_number = int(input())
    total = total + current_number
    if current_number > max_number:
        max_number = current_number
if total / 2 == max_number:
    print("Yes")
    print(f"Sum = {max_number}")
else:
    diff = abs(max_number - (total - max_number))
    print("No")
    print(f"Diff = {diff}")
