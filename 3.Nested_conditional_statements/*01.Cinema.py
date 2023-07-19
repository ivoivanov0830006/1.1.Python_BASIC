type_movie = input()
rows = int(input())
columns = int(input())
price = 0

if type_movie == "Premiere":
    price = 12
elif type_movie == "Normal":
    price = 7.5
elif type_movie == "Discount":
    price = 5
    
total = rows * columns * price
print(f"{total:.2f} leva")
