n = int(input())
total20 = 0
total40 = 0
total60 = 0
total80 = 0
total100 = 0

for numbers in range(1, n+1):
    current_number = int(input())
    if current_number < 200:
        total20 = total20 + 1
    elif 200 <= current_number < 400:
        total40 = total40 + 1
    elif 400 <= current_number < 600:
        total60 = total60 + 1
    elif 600 <= current_number < 800:
        total80 = total80 + 1
    elif 800 <= current_number:
        total100 = total100 + 1
        
print(f"{((total20 / n) * 100):.2f}%")
print(f"{((total40 / n) * 100):.2f}%")
print(f"{((total60 / n) * 100):.2f}%")
print(f"{((total80 / n) * 100):.2f}%")
print(f"{((total100 / n) * 100):.2f}%")
