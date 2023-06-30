import math
figure = input()
area = 0
if figure == "square":
    a = float(input())
    area = a * a
elif figure == "rectangle":
    a = float(input())
    b = float(input())
    area = a * b
elif figure == "circle":
    a = float(input())
    area = math.pi * (a ** 2)
elif figure == "triangle":
    a = float(input())
    b = float(input())
    area = a * b / 2
print("{:.3f}".format(area))
