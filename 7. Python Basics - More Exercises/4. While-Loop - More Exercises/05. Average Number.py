n = int(input())

count = 0
sum_number = 0

number = int(input())

for i in range(1, n + 1):
    number = int(number)
    count += 1
    sum_number += number

    if i == n:
        break

    number = int(input())

print(f"{sum_number/count:.2f}")