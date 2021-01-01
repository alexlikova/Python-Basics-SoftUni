recording_time, number_of_scenes, time_one_scene = [int(input()) for _ in range(3)]

preparation_time = recording_time * 0.15

recording_time_all = (number_of_scenes * time_one_scene) + preparation_time

diff = abs(recording_time - recording_time_all)

if recording_time_all <= recording_time:
    print(f"You managed to finish the movie on time! You have {diff:.0f} minutes left!")
else:
    print(f"Time is up! To complete the movie you need {diff:.0f} minutes.")