n = int(input())
l = int(input())

for first_digit in range(1, n):
    for second_digit in range (1, n):
        for third_digit in range(97, 97 + l):
            third_digit = chr(third_digit)
            for forth_digit in range(97, 97 + l):
                forth_digit = chr(forth_digit)
                for fifth_digit in range(1, n + 1):
                    if fifth_digit > first_digit and fifth_digit > second_digit:

                        print(f"{first_digit}{second_digit}{third_digit}{forth_digit}{fifth_digit}", end=" ")