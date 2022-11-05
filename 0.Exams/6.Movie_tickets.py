command = input()
total_student = 0
total_standard = 0
total_kid = 0
total_tickets = 0
while command != "Finish":
    movie = command
    current_total = 0
    free_spaces = int(input())
    input_line = input()
    while input_line != "End":
        ticket_type = input_line
        current_total += 1
        if ticket_type == "student":
            total_student += 1
        elif ticket_type == "standard":
            total_standard += 1
        elif ticket_type == "kid":
            total_kid += 1
        if current_total == free_spaces:
            break
        input_line = input()
    percentage_hall = current_total / free_spaces * 100
    print(f"{movie} - {percentage_hall:.2f}% full.")
    command = input()
total_tickets = total_kid + total_standard + total_student
print(f"Total tickets: {total_tickets}")
student_percentage = total_student / total_tickets * 100
print(f"{student_percentage:.2f}% student tickets.")
standard_percentage = total_standard / total_tickets * 100
print(f"{standard_percentage:.2f}% standard tickets.")
kid_percentage = total_kid / total_tickets * 100
print(f"{kid_percentage:.2f}% kids tickets.")
