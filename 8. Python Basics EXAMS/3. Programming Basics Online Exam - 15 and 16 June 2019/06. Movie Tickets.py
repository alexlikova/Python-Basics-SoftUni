a1, a2, n = [int(input()) for _ in range(3)]

for first in range(a1, a2):
    for second in range(1, n):
        until = int(n / 2)
        for third in range(1, until):
            forth = first
            total = second + third + forth
            if first % 2 != 0 and total % 2 != 0:
                print(f"{chr(first)}-{second}{third}{forth}")