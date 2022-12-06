minutes_control = int(input())
seconds_control = int(input())
length_in_meters = float(input())
seconds_for_hundred_meters = int(input())
control_in_seconds = minutes_control * 60 + seconds_control
reduction_time_in_seconds = length_in_meters / 120 * 2.5
competitor_time = length_in_meters / 100 * seconds_for_hundred_meters - reduction_time_in_seconds
if competitor_time <= control_in_seconds:
    print("Marin Bangiev won an Olympic quota!")
    print(f"His time is {competitor_time:.3f}.")
else:
    diff = competitor_time - control_in_seconds
    print(f"No, Marin failed! He was {diff} second slower.")
