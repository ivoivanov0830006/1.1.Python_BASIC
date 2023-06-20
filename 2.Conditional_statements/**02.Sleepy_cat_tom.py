rest_days = int(input())
work_days = 365 - rest_days
time_year = 30000
time_day = time_year / 365
play_time = rest_days * 127 + work_days * 63
if play_time > time_year:
    hours = (play_time - time_year) // 60
    minutes = (play_time - time_year) % 60
    print("Tom will run away")
    print(f"{hours} hours and {minutes} minutes more for play")
else:
    hours = (time_year - play_time) // 60
    minutes = (time_year - play_time) % 60
    print("Tom sleeps well")
    print(f"{hours} hours and {minutes} minutes less for play")
