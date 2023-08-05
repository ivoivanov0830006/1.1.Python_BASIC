name = input()
current_grade = 1
average_score = 0
total_score = 0
total_fails = 0

while current_grade <= 12:
    current_score = float(input())
    if current_score >= 4:
        current_grade += 1
        total_score += current_score
    else:
        current_grade += 0
        total_score += 0
        total_fails += 1
        if total_fails == 2:
            break
if total_fails < 2:
    average_score = total_score / 12
    print(f"{name} graduated. Average grade: {average_score:.2f}")
else:
    print(f"{name} has been excluded at {current_grade} grade")


# student_name = input()
# current_class = 1
# total_fails = 0
# total_grade = 0
# is_excluded = False
# while current_class <= 12:
#     current_grade = float(input())
#     if current_grade < 4:
#         total_fails += 1
#         if total_fails > 1:
#             is_excluded = True
#             break
#         continue
#     current_class += 1
#     total_grade += current_grade
# if is_excluded:
#     print(f"{student_name} has been excluded at {current_class} grade")
# else:
#     average_score = total_grade / 12
#     print(f"{student_name} graduated. Average grade: {average_score:.2f}")
