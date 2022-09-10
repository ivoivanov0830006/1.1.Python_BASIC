number = int(input())
max_number = int(input())
special_number = int(input())

for address in range(max_number, number - 1, -1):
    if address % 2 == 0 and address % 3 == 0:
        if special_number % 2 == 0 and special_number % 3 == 0:
            if address <= special_number:
                break
            elif address > special_number:
                print(address, end=" ")
        else:
            print(address, end=" ")
