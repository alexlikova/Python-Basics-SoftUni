n = int(input())

count_numbers_div_2 = 0
count_numbers_div_3 = 0
count_numbers_div_4 = 0
for number in range(1, n + 1):
    numbers = int(input())
    if numbers % 2 == 0:
        count_numbers_div_2 += 1
    if numbers % 3 == 0:
        count_numbers_div_3 += 1
    if numbers % 4 == 0:
        count_numbers_div_4 += 1

p1 = count_numbers_div_2 / n * 100
p2 = count_numbers_div_3 / n * 100
p3 = count_numbers_div_4 / n * 100

print(f"{p1:.2f}%\n{p2:.2f}%\n{p3:.2f}%")
