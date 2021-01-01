
def week(i):
    switcher = {
        7: 'Sunday',
        1: 'Monday',
        2: 'Tuesday',
        3: 'Wednesday',
        4: 'Thursday',
        5: 'Friday',
        6: 'Saturday'
    }
    return switcher.get(i, "Error")

number = int(input())

day_name = week(number)
print(day_name)