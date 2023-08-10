total_number = int(input())
total = 0

while total != total_number:
    number = int(input())
    total += number
    if total >= total_number:
        break
print(f"{total}")

# control_number = int(input())
# sum_of_numbers = 0
#
# while sum_of_numbers < control_number:
#     current_number = int(input())
#     sum_of_numbers += current_number
# print(sum_of_numbers)

