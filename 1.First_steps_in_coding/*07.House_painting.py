x = float(input())
y = float(input())
h = float(input())

green = 1 / 3.4
red = 1 / 4.3
window = float(1.5 ** 2)
door = 1.2 * 2
front = (x ** 2) - door
back = x ** 2
sides = 2 * (x * y - window)
roof = x * y * 2 + (x * h)
green_paint = float((front + back + sides) * green)
red_paint = float(roof * red)

print("{:.2f}".format(green_paint))
print("{:.2f}".format(red_paint))
