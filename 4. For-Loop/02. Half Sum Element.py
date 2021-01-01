import sys

n = int(input())

max_num = -sys.maxsize #създаваме максимална стойнст, която ще проверяваме дали сумата от останалите е равна на нея
sum_numbers = 0

for number in range(1, n + 1):
    value = int(input())
    sum_numbers += value
    if value > max_num:
        max_num = value

if (max_num == sum_numbers - max_num):
    print(f"Yes\nSum = {max_num}")
else:
    print(f"No\nDiff = {abs(max_num - (sum_numbers - max_num))}")