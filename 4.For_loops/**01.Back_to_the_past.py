money = float(input())
year = int(input())
age = 0
diff = 0
spend = 0

for current_year in range(1800, year + 1, 1):
    diff = current_year - 1800
    age = 18 + diff
    if current_year % 2 == 0:
        spend = 12000
        money -= spend
    else:
        spend = 12000 + 50 * age
        money -= spend
        
if money >= 0:
    print(f"Yes! He will live a carefree life and will have {money:.2f} dollars left.")
else:
    print(f"He will need {(abs(money)):.2f} dollars to survive.")
