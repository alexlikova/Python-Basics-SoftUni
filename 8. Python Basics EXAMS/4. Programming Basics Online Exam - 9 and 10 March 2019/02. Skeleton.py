minutes_controlla = int(input())
seconds_controlla = int(input())
distance_m = float(input())
seconds_100_m = int(input())

controlla_in_sec = minutes_controlla * 60 + seconds_controlla
decrease_time = distance_m / 120
total_decrease_time = decrease_time * 2.5
time_Marin = (distance_m / 100) * seconds_100_m - total_decrease_time

diff = time_Marin - controlla_in_sec
if time_Marin <= controlla_in_sec:
    print(f"Marin Bangiev won an Olympic quota!\nHis time is {time_Marin:.3f}.")
else:
    print(f"No, Marin failed! He was {diff:.3f} second slower.")
