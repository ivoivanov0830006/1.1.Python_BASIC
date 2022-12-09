shooting_time = int(input())
scenes_count = int(input())
scene_time = int(input())
preparing_time = 0.15 * shooting_time

total_time = preparing_time + scenes_count * scene_time

diff = abs(round(total_time - shooting_time))

if total_time <= shooting_time:
    print(f"You managed to finish the movie on time! You have {diff} minutes left!")
else:
    print(f"Time is up! To complete the movie you need {diff} minutes.")
