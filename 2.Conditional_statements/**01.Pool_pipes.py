volume = int(input())
pipe1 = int(input())
pipe2 = int(input())
hours = float(input())
total_volume = (pipe1 + pipe2) * hours
if total_volume <= volume:
    pool_percent = (total_volume / volume) * 100
    pipe1_percent = ((pipe1 * hours) / total_volume) * 100
    pipe2_percent = ((pipe2 * hours) / total_volume) * 100
    print(f"The pool is {pool_percent:.2f}% full. Pipe 1: {pipe1_percent:.2f}%. Pipe 2: {pipe2_percent:.2f}%")
else:
    over_volume = total_volume - volume
    print(f"For {hours} hours the pool overflow with {over_volume:.2f} liters")
