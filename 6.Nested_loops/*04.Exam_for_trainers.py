judges_count = int(input())
presentation = input()
total_score = 0
presentation_count = 0

while presentation != "Finish":
    presentation_count += 1
    current_total_score = 0
    for judge in range(1, judges_count + 1):
        score = float(input())
        current_total_score += score
    total_score += current_total_score
    average = current_total_score / judges_count
    print(f"{presentation} - {average:.2f}.")
    presentation = input()
assessment = total_score / (judges_count * presentation_count)
print(f"Student's final assessment is {assessment:.2f}.")
