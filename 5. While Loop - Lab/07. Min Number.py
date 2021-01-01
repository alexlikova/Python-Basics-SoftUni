import sys

number_text = input()

min = sys.maxsize
while number_text != "Stop":
    number = int(number_text)
    if number < min:
        min = number
    number_text = input()

print(min)