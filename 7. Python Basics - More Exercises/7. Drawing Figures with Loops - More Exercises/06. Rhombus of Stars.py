n = int(input()) # n=3

for row in range(1, n): # row = 1, row = 2
    print(f"{' ' * (n - row)}*{(row - 1) * ' *'}")
print("* " * n)
for column in range(n - 1, 0, -1): # column = 1
    print(f"{' ' * (n - column)}*{(column - 1) * ' *'}")

"""

n = int(input())
[print(f'{" " * (n - r) }{"* " * r}')for r in range(1, n + 1)]
[print(f'{" " * r }{"* " * (n - r)}')for r in range(1, n)]
"""