import math

n = int(input()) # прочитаме степента, която искаме да се вдигне числото

for power in range(0, n +1): # от 0-та степен до n-та степен
    if power % 2 == 0:
        print((2 ** power))

"""
n = int(input()) # прочитаме степента, която искаме да се вдигне числото

for power in range(0, n +1, 2): # от 0-та степен до n-та степен
    print(math.pow(2, power))
"""