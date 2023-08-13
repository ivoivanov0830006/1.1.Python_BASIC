line_input = input()
total_count_tickets = 0
student_count = 0
standard_count = 0
kid_count = 0

while line_input != "Finish":
    movie = line_input
    current_movie_count = 0
    capacity = int(input())
    command_line = input()

    while command_line != "End":
        type_ticket = command_line
        total_count_tickets += 1
        current_movie_count += 1
        if type_ticket == "student":
            student_count += 1
        if type_ticket == "standard":
            standard_count += 1
        if type_ticket == "kid":
            kid_count += 1
        if current_movie_count == capacity:
            break
        command_line = input()
    percentage = (current_movie_count / capacity) * 100
    print(f"{movie} - {percentage:.2f}% full.")
    line_input = input()
print(f"Total tickets: {total_count_tickets}")
percentage_student = student_count / total_count_tickets * 100
print(f"{percentage_student:.2f}% student tickets.")
percentage_standard = standard_count / total_count_tickets * 100
print(f"{percentage_standard:.2f}% standard tickets.")
percentage_kid = kid_count / total_count_tickets * 100
print(f"{percentage_kid:.2f}% kids tickets.")
