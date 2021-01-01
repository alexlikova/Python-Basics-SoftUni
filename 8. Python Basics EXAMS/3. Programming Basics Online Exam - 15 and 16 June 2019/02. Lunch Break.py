import math

movie_name = input()
time_episode = int(input())
total_time_lunch_break = int(input())

time_for_lunch = total_time_lunch_break * 1/8
time_for_rest = total_time_lunch_break * 1/4
left_time = total_time_lunch_break - time_for_lunch - time_for_rest

diff = math.ceil(abs(left_time - time_episode))
if left_time >= time_episode:
    print(f"You have enough time to watch {movie_name} and left with {diff:.0f} minutes free time.")
else:
    print(f"You don't have enough time to watch {movie_name}, you need {diff:.0f} more minutes.")