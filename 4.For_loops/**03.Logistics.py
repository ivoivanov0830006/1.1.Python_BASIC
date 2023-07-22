loads_count = int(input())

price_van = 0
price_truck = 0
price_train = 0
total_load_van = 0
total_load_truck = 0
total_load_train = 0

for loads in range(1, loads_count + 1):
    load = int(input())
    if load <= 3:
        price_van = 200
        total_load_van += load
    elif 3 < load <= 11:
        price_truck = 175
        total_load_truck += load
    else:
        price_train = 120
        total_load_train += load
        
total_load = total_load_van + total_load_truck + total_load_train
total_cost = total_load_van * price_van + total_load_truck * price_truck + total_load_train * price_train
average_cost = total_cost / total_load
percentage_van = total_load_van / total_load * 100
percentage_truck = total_load_truck / total_load * 100
percentage_train = total_load_train / total_load * 100

print(f"{average_cost:.2f}")
print(f"{percentage_van:.2f}%")
print(f"{percentage_truck:.2f}%")
print(f"{percentage_train:.2f}%")
