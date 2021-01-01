
def ticket(i):
    switcher = {
        'sunday': 16, 'saturday': 16,
        'monday': 12, 'tuesday': 12, 'friday': 12,
        'wednesday': 14, 'thursday': 14
        }
    return switcher.get(i, "Error")

day = str(input()).lower()
result = ticket(day)
print(result)
