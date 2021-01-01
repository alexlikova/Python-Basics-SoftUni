n = int(input())

if 2 <= n <= 10000:
    for a in range(1, 10):
        for b in range(1, 10):
            for c in range(1, 10):
                for d in range(1, 10):
                    if a + b == c + d:
                        if (n % (a + b)) == 0:
                            print(f"{a}{b}{c}{d}", end=" ")

"""
from itertools import  product
divider = int(input())

for el in map(str,product(range(1,10), repeat = 4)):
    concat = ''.join(filter(lambda y: y.isdigit(), el))
    if sum(map(int, concat[:2])) == sum(map(int, concat[2:])):
        if divider %  sum(map(int, concat[:2])) == 0:
            print(concat, end=' ')
"""