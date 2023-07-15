age = float(input())
sex = input()
if sex == "m" and age >= 16:
    print("Mr.")
if sex == "m" and age < 16:
    print("Master")
if sex == "f" and age >= 16:
    print("Ms.")
if sex == "f" and age < 16:
    print("Miss")

# age = float(input())
# sex = input()
# if gender == "m":
#     if age >= 16:
#         print("Mr.")
#     else:
#         print("Master")
# elif gender == "f":
#     if age >= 16:
#         print("Ms.")
#     else:
#         print("Miss")
