for hour in range(0, 24):
    for minute in range(0, 60):
        if minute < 10:
            print(f'{hour}:0{minute}')
        else:
            print(f'{hour}:{minute}')
