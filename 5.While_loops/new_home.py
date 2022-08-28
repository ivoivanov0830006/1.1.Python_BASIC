width = int(input())
length = int(input())
height = int(input())
total_volume = width * length * height
total_box_volume = 0
command = input()
total_box_count = 0
is_full = False

while command != "Done":
    current_box = int(command)
    total_box_count += current_box
    total_box_volume = total_box_count
    if total_box_volume > total_volume:
        is_full = True
        break
    command = input()
diff = abs(total_box_volume - total_volume)
if is_full:
    print(f"No more free space! You need {diff} Cubic meters more.")
if command == "Done":
    print(f"{diff} Cubic meters left.")
