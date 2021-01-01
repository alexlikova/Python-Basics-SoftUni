"""
hour_exam = int(input()) # 0...23
min_exam = int(input()) # 0...59
hour_arrival = int(input())
min_arrival = int(input())

total_min_exam = (hour_exam * 60) + min_exam # 9:30 exam --> 570 min
total_min_arrival = (hour_arrival * 60) + min_arrival # 9.00 arrival --> 540 min // 8.30 arrival --> 510 min

difference = total_min_arrival - total_min_exam

if (difference < -30):
    print("Early")
elif 0 >= difference >= -30: # 9.00exam --> arrival 8.30am 8.40am ---> 540 min (510min (-30min earlier),
    print("On time")
else:
    print("Late")

if total_min_exam - 60 < total_min_arrival < total_min_exam:
    print(f"{abs(difference)} minutes before the start")

elif total_min_arrival <= total_min_exam - 60:
    hour = abs(difference)//60
    min = abs(difference)%60

    if min <= 9:
       print(f"{hour}:{min:02d} hours before the start") # 2 decimals after the . --> but 1st one is always 0
    else:
        print(f"{hour}:{min} hours before the start")

elif total_min_exam < total_min_arrival < total_min_exam + 60:
    print(f"{difference} minutes after the start")

elif total_min_arrival >= total_min_exam + 60:
    hour = abs(difference) // 60
    min = abs(difference) % 60

    if min <= 9:
        print(f"{hour}:{min:02d} hours after the start")  # 2 decimals after the . --> but 1st one is always 0
    else:
        print(f"{hour}:{min} hours after the start")

"""

"""
exam_hour = int(input())
exam_minute = int(input())
arrival_hour = int(input())
arrival_minute = int(input())
status = ''
exam_time = (exam_hour * 60) + exam_minute       #540
arrival_time = (arrival_hour * 60) + arrival_minute #520
total_time_difference = exam_time - arrival_time    #рано с 20 мин
if total_time_difference > 30:
    status = 'Early'
    if total_time_difference < 60:
        print(f'{status}')
        print(f'{abs(total_time_difference)} minutes before the start')
    else:
        total_minutes = total_time_difference % 60
        total_hours = total_time_difference / 60
        total_hours = int(total_hours)
        if total_minutes < 10:
            print(f'{status}')
            print(f'{total_hours}:0{total_minutes:02d} hours before the start')
        else:
            print(f'{status}')
            print(f'{total_hours}:{total_minutes:02d} hours before the start')
elif 0 <= total_time_difference <= 30:
    status = 'On time'
    if total_time_difference == 0:
        print(f'{status}')
    else:
        print(f'{status}')
        print(f'{total_time_difference} minutes before the start')
else:
    status = 'Late'
    if total_time_difference >= -59:
        print(f'{status}')
        print(f'{abs(total_time_difference)} minutes after the start')
    else:
        total_minutes = total_time_difference % 60
        total_hours = total_time_difference / 60
        total_hours = int(total_hours)
        if total_minutes < 10:
            print(f'{status}')
            print(f'{abs(total_hours)}:0{total_minutes:02d} hours after the start')
        else:
            print(f'{status}')
            print(f'{abs(total_hours)}:{total_minutes:02d} hours after the start')
"""

ex_hour, ex_min, ar_hour, ar_min = [int(input()) for _ in range(4)]

exam_min = ex_min + ex_hour * 60
arrive_min = ar_min + ar_hour * 60

if arrive_min > exam_min:
    print("Late")
elif exam_min - arrive_min <= 30:
    print("On time")
else:
    print("Early")

result = abs(exam_min - arrive_min)
if exam_min - arrive_min > 0:
    if result < 60:
        print(f"{result} minutes before the start")
    else:
        print(f"{result // 60}:{result % 60:02d} hours before the start")
elif arrive_min - exam_min > 0:
    if result < 60:
        print(f"{result} minutes after the start")
    else:
        print(f"{result // 60}:{result % 60:02d} hours after the start")


