command = input()
movie_name = ""
movie_count = 0
best_points = 0
best_movie = ""
total_points = 0
limit_is_reached = False

while command != "STOP":
    total_points = 0
    movie_count += 1
    if movie_count == 7:
        limit_is_reached = True
        break
    movie_name = command
    for letter in movie_name:
        current_points = 0
        if letter.isupper():
            current_points = ord(letter) - len(movie_name)
        elif letter.islower():
            current_points = ord(letter) - 2 * len(movie_name)
        else:
            current_points = ord(letter)
        total_points += current_points
    if total_points > best_points:
        best_points = total_points
        best_movie = movie_name
    command = input()

if limit_is_reached:
    print(f"The limit is reached.")
print(f"The best movie for you is {best_movie} with {best_points} ASCII sum.")
