from math import floor

movie_name = input()
seasons = int(input())
episodes = int(input())
time_per_episode = float(input())
time_per_episode *= 1.20
special_episodes = seasons * 10
total_time = seasons * episodes * time_per_episode + special_episodes
print(f"Total time needed to watch the {movie_name} series is {floor(total_time)}")
