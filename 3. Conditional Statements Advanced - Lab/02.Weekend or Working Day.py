"""
input = str(input().lower())

if (input == "monday" or input == "tuesday" or input == "wednesday" or input == "thursday" or input == "friday"):
    print("Working day")

elif (input == "saturday" or input == "sunday"):
    print("Weekend")

else:
    print("Error")
"""

#working_day = "monday", "tuesday", "wednesday", "thursday", "friday"
#weekend = "saturday", "sunday"

working_day = "Working day"
weekend = "Weekend"
def day (i):
    switcher = {
        'sunday': weekend,
        'monday': working_day,
        'tuesday': working_day,
        'wednesday': working_day,
        'thursday': working_day,
        'friday': working_day,
        'saturday': weekend
    }
    return switcher.get(i, "Error")

input = str(input().lower())

day_name = day(input)
print(day_name)
