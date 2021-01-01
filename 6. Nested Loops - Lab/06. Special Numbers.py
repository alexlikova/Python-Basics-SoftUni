number = int(input())

for numbers in range(1111, 10000):
    is_magic = True
    numbers_as_string = str(numbers)
    for digit in numbers_as_string:
        if int(digit) == 0 or number % int(digit) != 0:
            is_magic = False
            break
    if is_magic:
        print(f"{numbers_as_string}", end=" ")