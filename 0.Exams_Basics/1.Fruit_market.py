strawberries_price = float(input())
bananas_kg = float(input())
oranges_kg = float(input())
raspberries_kg = float(input())
strawberries_kg = float(input())

raspberries_price = strawberries_price / 2
oranges_price = 0.6 * raspberries_price
bananas_price = 0.2 * raspberries_price

total_strawberries = strawberries_kg * strawberries_price
total_bananas = bananas_kg * bananas_price
total_oranges = oranges_kg * oranges_price
total_raspberries = raspberries_kg * raspberries_price

total = total_oranges + total_raspberries + total_bananas + total_strawberries

print(f"{total:.2f}")
