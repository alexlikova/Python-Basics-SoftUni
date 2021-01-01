import math

n = int(input())

if n == 1 or n == 2:
    print(f"{'*' * n}")

leftright = math.floor((n - 1) / 2)  # (3 - 1) / 2 = 1 line

# 1st row
if 3 <= 100:
    if n % 2 == 0:  # even number
        stars = 2
    else:
        stars = 1
    print(f"{'-' * leftright}{stars * '*'}{'-' * leftright}")

# next rows to the middle
if n % 2 == 0:
    for next_rows_middle in range(1, 3):
        leftright -= 1
        stars = 1
        mid = n - 2 * leftright - 2
        if mid >= 0:
            print(f"{'-' * leftright}{stars * '*'}{mid * '-'}{stars * '*'}{'-' * leftright}")

# from middle to the bottom
for next_rows_middle in range(3, 1), -1:
    leftright += 1
    stars = 1
    mid = n - 2 * leftright - 2
    if mid >= 0:
        print(f"{'-' * leftright}{stars * '*'}{mid * '-'}{stars * '*'}{'-' * leftright}")

"""
n = int(input())  # n=3

for row in range(1, n):  # row = 1, row = 2
    print(f"{'_' * (n - row)}*{(row - 1) * ' *'}{'_' * (n - row)}")
print("* " * n)
# for column in range(n - 1, 0, -1): # column = 1
# print(f"{' ' * (n - column)}*{(column - 1) * ' *'}")
"""
