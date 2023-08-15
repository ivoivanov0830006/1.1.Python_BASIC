weight_kg = float(input())
package_type = input()
distance = int(input())
price = 0

if package_type == "standard":
    if weight_kg < 1:
        price = 0.03
    elif weight_kg < 10:
        price = 0.05
    elif weight_kg < 40:
        price = 0.1
    elif weight_kg < 90:
        price = 0.15
    elif weight_kg < 150:
        price = 0.2
elif package_type == "express":
    if weight_kg < 1:
        price = 0.03 + weight_kg * (0.03 * 0.8)
    elif weight_kg < 10:
        price = 0.05 + weight_kg * (0.05 * 0.4)
    elif weight_kg < 40:
        price = 0.1 + weight_kg * (0.1 * 0.05)
    elif weight_kg < 90:
        price = 0.15 + weight_kg * (0.15 * 0.02)
    elif weight_kg < 150:
        price = 0.2 + weight_kg * (0.2 * 0.01)

total_price = price * distance

print(f"The delivery of your shipment with weight of {weight_kg:.3f} kg. would cost {total_price:.2f} lv.")
