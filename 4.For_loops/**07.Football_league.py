capacity =  int(input())
total_guests = int(input())

total_a = 0
total_b = 0
total_v = 0
total_g = 0

for guest in range(1, total_guests + 1):
    sector = input()
    if sector == "A":
        total_a = total_a + 1
    elif sector == "B":
        total_b = total_b + 1
    elif sector == "V":
        total_v = total_v + 1
    elif sector == "G":
        total_g = total_g + 1
percent_a = total_a / total_guests * 100
percent_b = total_b / total_guests * 100
percent_v = total_v / total_guests * 100
percent_g = total_g / total_guests * 100
percent_stadium = total_guests / capacity * 100

print(f"{percent_a:.2f}%")
print(f"{percent_b:.2f}%")
print(f"{percent_v:.2f}%")
print(f"{percent_g:.2f}%")
print(f"{percent_stadium:.2f}%")
