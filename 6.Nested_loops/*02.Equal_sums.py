start_number = int(input())
end_number = int(input())

for number in range(start_number, end_number + 1):
    current_number = str(number)
    even_sum = 0
    odd_sum = 0
    for symbol in range(0, len(current_number)):
        digit = int(current_number[symbol])  # simvola na konkretnata poziciq prevarnat v cqlo chislo
        if symbol % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit
    if even_sum == odd_sum:
        print(current_number, end = " ")
