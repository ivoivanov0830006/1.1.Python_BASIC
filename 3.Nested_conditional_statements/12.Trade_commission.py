city = input()
sales = float(input())
commission = 0
total = 0

if city == "Sofia":
    if 0 <= sales <= 500:
        commission = 0.05
        total = commission * sales
        print(f"{total:.2f}")
    elif 500 < sales <= 1000:
        commission = 0.07
        total = commission * sales
        print(f"{total:.2f}")
    elif 1000 < sales <= 10000:
        commission = 0.08
        total = commission * sales
        print(f"{total:.2f}")
    elif sales > 10000:
        commission = 0.12
        total = commission * sales
        print(f"{total:.2f}")
    else:
        print("error")
elif city == "Varna":
    if 0 <= sales <= 500:
        commission = 0.045
        total = commission * sales
        print(f"{total:.2f}")
    elif 500 < sales <= 1000:
        commission = 0.075
        total = commission * sales
        print(f"{total:.2f}")
    elif 1000 < sales <= 10000:
        commission = 0.10
        total = commission * sales
        print(f"{total:.2f}")
    elif sales > 10000:
        commission = 0.13
        total = commission * sales
        print(f"{total:.2f}")
    else:
        print("error")
elif city == "Plovdiv":
    if 0 <= sales <= 500:
        commission = 0.055
        total = commission * sales
        print(f"{total:.2f}")
    elif 500 < sales <= 1000:
        commission = 0.08
        total = commission * sales
        print(f"{total:.2f}")
    elif 1000 < sales <= 10000:
        commission = 0.12
        total = commission * sales
        print(f"{total:.2f}")
    elif sales > 10000:
        commission = 0.145
        total = commission * sales
        print(f"{total:.2f}")
    else:
        print("error")
else:
    print("error")
