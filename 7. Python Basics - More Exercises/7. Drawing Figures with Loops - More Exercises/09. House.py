import math

n = int(input())

roof_rows = int((n + 1) / 2)
base_rows = int(n / 2 - 1)
stars = 0

# 1st row roof
if n % 2 == 0:
    stars = 2
else:
    stars = 1
# 1st row roof
lines = math.floor((n - 1) / 2) # (3 - 1) / 2 = 1 line
print(f"{'-' * lines}{stars * '*'}{'-' * lines}")

# next rows roof
for rows_roof in range(1, roof_rows):
    stars += 2
    lines -= 1
    print(f"{'-' * lines}{stars * '*'}{'-' * lines}")

# house base
for rows_base in range(0, base_rows + 1):
    print(f"|{(n - 2) * '*'}|")
