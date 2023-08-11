control_number = int(input())
count = 0
is_enough_for_password = False
password_number = 0


for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                if a < b and c > d and a * b + c * d == control_number:
                    count += 1
                    if count == 4:
                        is_enough_for_password = True
                        password_number = a*1000+b*100+c*10+d
                    print(f"{a}{b}{c}{d}", end=" ")
if is_enough_for_password:
    print(f"\nPassword: {password_number}")
else:
    print("\nNo!")
