points = int(input())
bonus = 0
if 100 >= points:
    bonus = 5
elif 1000 >= points > 100:
    bonus = 0.2 * points
elif 1000 < points:
    bonus = 0.1 * points
if points % 2 == 0:
    bonus = bonus + 1
elif points % 10 == 5:
    bonus = bonus + 2
print(bonus)
print(bonus + points)

# number = int(input())
# bonus = 0
# if number <= 100:
#     bonus = 5
# elif number <= 1000:
#     bonus = number * 0.2
# else:
#     bonus = number * 0.1
#
# if number % 2 == 0:
#     bonus = bonus + 1
# elif number % 10 == 5:
#     bonus = bonus + 2
#
# total = number + bonus
# print(bonus)
# print(total)


