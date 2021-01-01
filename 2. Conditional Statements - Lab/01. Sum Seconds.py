import math
"""
time_first = int(input());
time_second = int(input());
time_third = int(input());
"""

time_first, time_second, time_third = [int(input()) for _ in range(3)]

total_time = time_first + time_second + time_third

min = math.floor(total_time / 60)
sec = total_time % 60

if sec < 10:
    print(f'{min}:0{sec}')
else:
    print(f'{min}:{sec}')

