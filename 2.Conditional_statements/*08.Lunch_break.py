import math
name = input()
episode_time = int(input())
total_time = int(input())
lunch_time = total_time / 8
free_time = total_time / 4
rest_time = total_time - lunch_time - free_time
diff = 0
if rest_time >= episode_time:
    diff = math.ceil(abs(rest_time - episode_time))
    print(f"You have enough time to watch {name} and left with {diff} minutes free time.")
else:
    diff = math.ceil(abs(rest_time - episode_time))
    print(f"You don't have enough time to watch {name}, you need {diff} more minutes.")
