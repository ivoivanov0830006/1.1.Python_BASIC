length = int(input())
width = int(input())
command = input()

total_pieces = 0
all_pieces = length * width
is_finished = False

while command != "STOP":
    current_pieces = int(command)
    total_pieces += current_pieces
    if total_pieces >= all_pieces:
        is_finished = True
        break
    command = input()
diff = abs(total_pieces - all_pieces)
if is_finished:
    print(f"No more cake left! You need {diff} pieces more.")
else:
    print(f"{diff} pieces are left.")
