height = int(input())
width = int(input())
percentage_non_painted = int(input())
all_m2 = 4 * height * width
total_area = all_m2 - all_m2 * percentage_non_painted / 100
current_area = total_area
command = input()
is_finished = False
is_perfect = False
liters = 0

while command != "Tired!":
    liters = int(command)
    current_area -= liters
    if current_area < 0:
        is_finished = True
        break
    elif current_area == 0:
        is_perfect = True
        break
    command = input()
if is_finished:
    rest_paint = abs(current_area)
    print(f"All walls are painted and you have {rest_paint:.0f} l paint left!")
elif is_perfect:
    print("All walls are painted! Great job, Pesho!")
else:
    print(f"{current_area:.0f} quadratic m left.")
