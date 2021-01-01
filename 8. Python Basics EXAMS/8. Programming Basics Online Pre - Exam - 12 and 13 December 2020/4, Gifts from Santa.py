n, m, s = [int(input()) for _ in range(3)]

for number in range(m, n, -1):
    if (number % 2 == 0) and (number % 3 == 0):
        if number == s:
            break
        print(number, end=" ")