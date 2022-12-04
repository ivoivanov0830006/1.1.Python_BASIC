guest_count = int(input())
total_shake = 0
total_bar = 0
total_legs = 0
total_back = 0
total_chest = 0
total_abs = 0
total = 0

for person in range(1, guest_count + 1):
    activity = input()
    if activity == "Protein bar":
        total_bar += 1
        total += 1
    elif activity == "Protein shake":
        total_shake += 1
        total += 1
    elif activity == "Legs":
        total_legs += 1
        total += 1
    elif activity == "Back":
        total_back += 1
        total += 1
    elif activity == "Chest":
        total_chest += 1
        total += 1
    elif activity == "Abs":
        total_abs += 1
        total += 1

total_train = total_abs + total_back + total_chest + total_legs
total_protein = total_shake + total_bar

percentage_train = total_train / total * 100
percentage_protein = total_protein / total * 100

print(f"{total_back} - back")
print(f"{total_chest} - chest")
print(f"{total_legs} - legs")
print(f"{total_abs} - abs")
print(f"{total_shake} - protein shake")
print(f"{total_bar} - protein bar")
print(f"{percentage_train:.2f}% - work out")
print(f"{percentage_protein:.2f}% - protein")
