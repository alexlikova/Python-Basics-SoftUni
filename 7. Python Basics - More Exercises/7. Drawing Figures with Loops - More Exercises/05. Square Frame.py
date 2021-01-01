
n = int(input())

print(f"+{' -' * (n - 2)} +")
for i in range(n - 2):
    print(f"|{' -' * (n - 2)} |")
print(f"+{' -' * (n - 2)} +")

"""
n = int(input())

[print(f'+{" -" * (n - 2)} +') for _ in range(1)]
[print(f'|{" -" * (n - 2)} |') for _ in range(1, n -1)]
[print(f'+{" -" * (n - 2)} +') for _ in range(1)]
"""

