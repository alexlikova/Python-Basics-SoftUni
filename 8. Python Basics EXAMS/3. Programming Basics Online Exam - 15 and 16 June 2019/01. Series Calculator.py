import math

serial_name = str(input())
number_of_seasons = int(input())
number_of_episodes = int(input())
min_one_episode_no_ads = float(input())

min_one_episode_with_ads = min_one_episode_no_ads * 1.2

total_watch_time_min = math.floor(
    (number_of_seasons * number_of_episodes * min_one_episode_with_ads) + (number_of_seasons * 10))

print(f"Total time needed to watch the {serial_name} series is {total_watch_time_min} minutes.")
