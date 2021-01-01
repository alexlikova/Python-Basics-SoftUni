import sys

n = int(input())

odd_sum = 0
even_sum = 0
odd_max = -sys.maxsize
even_max = -sys.maxsize
odd_min = sys.maxsize
even_min = sys.maxsize

for number in range(1, n + 1):
    value = float(input())
    if number % 2 == 0:
        even_sum += value

        if (value > even_max):
            even_max = value
        if value < even_min:
            even_min = value
    else:
        odd_sum += value

        if (value > odd_max):
            odd_max = value
        if value < odd_min:
            odd_min = value

print(f"OddSum={odd_sum:.2f},")

if odd_min == sys.maxsize:
    print("OddMin=No,")
else:
    print(f"OddMin={odd_min:.2f},")

if (odd_max == -sys.maxsize):
    print("OddMax=No,")
else:
    print(f"OddMax={odd_max:.2f},")

print(f"EvenSum={even_sum:.2f},")
if even_min == sys.maxsize:
    print("EvenMin=No,")
else:
    print(f"EvenMin={even_min:.2f},")

if (even_max == -sys.maxsize):
    print("EvenMax=No")
else:
    print(f"EvenMax={even_max:.2f}")

