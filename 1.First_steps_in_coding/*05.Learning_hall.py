w = float(input())
h = float(input())
desk_w = 1.2
desk_h = 0.7
corridor = 1

columns = int((h - corridor) // desk_h)
rows = int(w // desk_w)
count = (columns * rows - 3)

print(count)


#w = float(input())
#h = float(input())
#area = w * h
#desk = 0.7 * 1.2
#corridor =  1
#door = desk
#front_desk = float(2 * desk)
#useable_area = area - corridor - door - front_desk
#desk_count = int(useable_area // desk)
#print(desk_count)
