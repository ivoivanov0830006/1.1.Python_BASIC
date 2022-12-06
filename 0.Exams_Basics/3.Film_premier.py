movie = input()
package = input()
tickets_count = int(input())
price = 0
discount = 1

if movie == "John Wick":
    if package == "Drink":
        price = 12
    elif package == "Popcorn":
        price = 15
    elif package == "Menu":
        price = 19
elif movie == "Star Wars":
    if package == "Drink":
        price = 18
    elif package == "Popcorn":
        price = 25
    elif package == "Menu":
        price = 30
    if tickets_count >= 4:
        discount = 0.7
elif movie == "Jumanji":
    if package == "Drink":
        price = 9
    elif package == "Popcorn":
        price = 11
    elif package == "Menu":
        price = 14
    if tickets_count == 2:
        discount = 0.85

total_price = price * tickets_count * discount

print(f"Your bill is {total_price:.2f} leva.")
