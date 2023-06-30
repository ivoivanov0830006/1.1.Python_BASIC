distance = int(input())
text = input()
taxi_start = 0.7
taxi_day = 0.79
taxi_night = 0.9
bus = 0.09
train = 0.06
cost_taxi_day = taxi_start + taxi_day * distance
cost_taxi_night = taxi_start + taxi_night * distance
cost_bus = bus * distance
cost_train = train * distance

if text == "day":
    if distance < 20:
        print(f"{cost_taxi_day:.2f}")
    elif distance < 100:
        print(f"{cost_bus:.2f}")
    else:
        print(f"{cost_train:.2f}")
elif text == "night":
    if distance < 20:
        print(f"{cost_taxi_night:.2f}")
    elif distance < 100:
        print(f"{cost_bus:.2f}")
    else:
        print(f"{cost_train:.2f}")
