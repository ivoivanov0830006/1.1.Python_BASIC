movie_name = input()
days = int(input())
tickets = int(input())
ticket_price = float(input())
cinema_cut = int(input())

profit = days * tickets * ticket_price
total_profit = profit - cinema_cut * profit / 100

print(f"The profit from the movie {movie_name} is {total_profit:.2f} lv.")
