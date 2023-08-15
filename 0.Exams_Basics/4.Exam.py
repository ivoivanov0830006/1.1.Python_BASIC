total_students = int(input())
top_count = 0
good_count = 0
average_count = 0
fail_count = 0

total_score = 0

for student in range(1, total_students + 1):
    score = float(input())
    total_score += score
    if score < 3:
        fail_count += 1
    elif score < 4:
        average_count += 1
    elif score < 5:
        good_count += 1
    elif score <= 6:
        top_count += 1

top_percentage = top_count / total_students * 100
good_percentage = good_count / total_students * 100
average_percentage = average_count / total_students * 100
fail_percentage = fail_count / total_students * 100
average_score = total_score / total_students

print(f"Top students: {top_percentage:.2f}%")
print(f"Between 4.00 and 4.99: {good_percentage:.2f}%")
print(f"Between 3.00 and 3.99: {average_percentage:.2f}%")
print(f"Fail: {fail_percentage:.2f}%")
print(f"Average: {average_score:.2f}")
