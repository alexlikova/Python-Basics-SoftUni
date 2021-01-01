n = int(input()) # n = 3

for rows in range(0, n + 1): # rows = 0, rows = 1, rows = 2, rows = 3
    print(f"{' ' * (n - rows)}{'*' * rows} | {'*' * rows}{' ' * (n - rows)}")