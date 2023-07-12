hour = int(input())
day = input()

if 10 > hour or 18 < hour or day == "Sunday":
    print("closed")
else:
    print("open")
