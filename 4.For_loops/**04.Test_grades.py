total_students = int(input())

total_grades = 0
students_perfect = 0
students_great = 0
students_good = 0
students_poor = 0

for student in range(1, total_students + 1):
    grades = float(input())
    if grades >= 5:
        students_perfect += 1
    elif grades >= 4:
        students_great += 1
    elif grades >= 3:
        students_good += 1
    else:
        students_poor += 1
    total_grades += grades

percent_perfect = students_perfect / total_students * 100
percent_great = students_great / total_students * 100
percent_good = students_good / total_students * 100
percent_poor = students_poor / total_students * 100
average = total_grades / total_students

print(f"Top students: {percent_perfect:.2f}%")
print(f"Between 4.00 and 4.99: {percent_great:.2f}%")
print(f"Between 3.00 and 3.99: {percent_good:.2f}%")
print(f"Fail: {percent_poor:.2f}%")
print(f"Average: {average:.2f}")
