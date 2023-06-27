import math
record = float(input())
distance = float(input())
distance_per_sec = float(input())
total_sec = distance * distance_per_sec
delay = 12.5
total_delay = math.floor(distance / 15) * delay
total_time = total_sec + total_delay
diff = 0
if record <= total_time:
    diff = abs(total_time - record)
    print(f"No, he failed! He was {diff:.2f} seconds slower.")
else:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
