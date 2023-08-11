start_interval = int(input())
end_interval = int(input())
magic_number = int(input())
current_combination = 0
is_found = False

for first_number in range(start_interval, end_interval + 1):
    for second_number in range(start_interval, end_interval + 1):
        current_combination += 1
        total_combinations = current_combination
        if first_number + second_number == magic_number:
            is_found = True
            break
    if is_found:
        break
if is_found:
    print(f"Combination N:{current_combination} ({first_number} + {second_number} = {magic_number})")
else:
    print(f"{total_combinations} combinations - neither equals {magic_number}")
