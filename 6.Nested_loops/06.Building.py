floors = int(input())
rooms = int(input())
room_label = ""

for floor in range(floors, 0, -1):
    for room in range(0, rooms):
        if floor == floors:
            room_label = "L"
        elif floor % 2 != 0:
            room_label = "A"
        elif floor % 2 == 0:
            room_label = "O"
        print(f"{room_label}{floor}{room}", end = " ")
    print()
