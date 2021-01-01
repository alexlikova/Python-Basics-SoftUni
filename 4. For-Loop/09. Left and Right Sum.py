n = int(input())

sum_one = 0
sum_two = 0
# сборът на първите n числа
for number in range(1, n + 1):
    value = int(input())
    sum_one += value

# сборът на вторите n числа
for number in range(1, n + 1):
    value = int(input())
    sum_two += value

# принтира резултата
if (sum_one == sum_two):
    print(f"Yes, sum = {sum_one}")
else:
    print(f"No, diff = {abs(sum_one - sum_two)}")