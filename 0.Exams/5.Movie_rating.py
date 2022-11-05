movies_count = int(input())
high_rating_movie = ""
highest_rating = 0
low_rating_movie = ""
lowest_rating = 10
total_rating = 0

for movie in range(1, movies_count + 1):
    movie_name = input()
    movie_rating = float(input())
    if movie_rating > highest_rating:
        high_rating_movie = movie_name
        highest_rating = movie_rating
    elif movie_rating < lowest_rating:
        low_rating_movie = movie_name
        lowest_rating = movie_rating
    total_rating += movie_rating
average = total_rating / movies_count
print(f"{high_rating_movie} is with highest rating: {highest_rating:.1f}")
print(f"{low_rating_movie} is with lowest rating: {lowest_rating:.1f}")
print(f"Average rating: {average:.1f}")
