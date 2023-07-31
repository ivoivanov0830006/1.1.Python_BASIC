group_count = int(input())
total1 = 0
total2 = 0
total3 = 0
total4 = 0
total5 = 0
total_people = 0

for group in range(1, group_count + 1):
    people = int(input())
    total_people += people
    if people <= 5:
        total1 = total1 + people
    elif people <= 12:
        total2 = total2 + people
    elif people <= 25:
        total3 = total3 + people
    elif people <= 40:
        total4 = total4 + people
    elif people > 40:
        total5 = total5 + people
        
total_musala = (total1 / total_people) * 100
total_monblan = (total2 / total_people) * 100
total_kilimandjaro = (total3 / total_people) * 100
total_k2 = (total4 / total_people) * 100
total_everest = (total5 / total_people) * 100

print(f"{total_musala:.2f}%")
print(f"{total_monblan:.2f}%")
print(f"{total_kilimandjaro:.2f}%")
print(f"{total_k2:.2f}%")
print(f"{total_everest:.2f}%")
