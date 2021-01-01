import sys

number_text = input()

# Действие --> пишене на числа и намиране най-ГОЛЯМОТО
# СТОП --> number_text == "STOP"
# CONTINUE --> number_text != "Stop"

max = - sys.maxsize
while number_text != "Stop":
    number = int(number_text)
    if number > max:
        max = number
    number_text = input()

print(max)