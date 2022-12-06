term = input()  # "one" or "two"
contract_type = input()   # "Small" "Middle" "Large" "ExtraLarge"
mobile_internet = input()   # "yes"   "no"
payable_months = int(input())
price = 0

if term == "one":
    if contract_type == "Small":
        price = 9.98
    elif contract_type == "Middle":
        price = 18.99
    elif contract_type == "Large":
        price = 25.98
    elif contract_type == "ExtraLarge":
        price = 35.99
elif term == "two":
    if contract_type == "Small":
        price = 8.58
    elif contract_type == "Middle":
        price = 17.09
    elif contract_type == "Large":
        price = 23.59
    elif contract_type == "ExtraLarge":
        price = 31.79
if mobile_internet == "yes":
    if price <= 10:
        price = price + 5.5
    elif price <= 30:
        price = price + 4.35
    else:
        price = price + 3.85
total_sum = price * payable_months
if term == "two":
    total_sum = total_sum * 0.9625

print(f"{total_sum:.2f} lv.")
