needed_height = int(input())
current_height = needed_height - 30
training_is_failed = False
is_completed = False
jumps_count = 0
jump_fails = 0
jump = int(input())

while not is_completed:
    jumps_count += 1
    if jump > needed_height:
        is_completed = True
        break
    if jump > current_height:
        jump_fails = 0
        current_height += 5
    else:
        jump_fails += 1
        if jump_fails == 3:
            training_is_failed = True
            break
    if training_is_failed:
        break
    jump = int(input())
if is_completed:
    print(f"Tihomir succeeded, he jumped over {current_height}cm after {jumps_count} jumps.")
if training_is_failed:
    print(f"Tihomir failed at {current_height}cm after {jumps_count} jumps.")


# ------------------------------------- Another Solution -----------------------------
#
# needed_height = int(input())
# current_height = needed_height - 30
# failed = False
# jumps_count = 0
# jump_fails = 0
# 
# while not failed:
#     jump = int(input())
#     jumps_count += 1
#     if jump <= current_height:
#         jump_fails += 1
#         if jump_fails == 3:
#             failed = True
#     else:
#         if current_height >= needed_height:
#             break
#         jump_fails = 0
#         current_height += 5
# 
# if not failed:
#     print(f"Tihomir succeeded, he jumped over {current_height}cm after {jumps_count} jumps.")
# else:
#     print(f"Tihomir failed at {current_height}cm after {jumps_count} jumps.")
