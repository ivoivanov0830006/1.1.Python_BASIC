start_first_pair = int(input())
start_second_pair = int(input())
diff_first_pair = int(input())
diff_second_pair = int(input())
end_first_pair = start_first_pair + diff_first_pair
end_second_pair = start_second_pair + diff_second_pair

for pair1 in range(start_first_pair, end_first_pair + 1):
    count_pair1 = 0
    for i in range(1, pair1 + 1):
        if pair1 % i == 0:
            count_pair1 += 1
    if count_pair1 == 2:

        for pair2 in range(start_second_pair, end_second_pair + 1):
            count_pair2 = 0
            for j in range(1, pair2 + 1):
                if pair2 % j == 0:
                    count_pair2 += 1
            if count_pair2 == 2:
                print(f"{pair1}{pair2}")
