from math import ceil
distance = 384400
total_distance = distance * 2
time_on_moon = 3
average_speed = float(input())
fuel_per_100 = float(input())
fuel_per_1 = fuel_per_100 / 100
time_flying = total_distance / average_speed

total_time = time_flying + time_on_moon
print(ceil(total_time))
total_fuel = fuel_per_1 * total_distance
print(int(total_fuel))
