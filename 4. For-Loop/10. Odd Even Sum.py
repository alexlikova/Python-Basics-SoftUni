n = int(input())

sum_even = 0
sum_odd = 0

for number in range(1, n + 1):
    value = int(input())
    if number % 2 ==0: # гледаме позизията дали е четна или нечетна
        sum_even += value
    else:
        sum_odd += value

if (sum_even == sum_odd):
    print(f"Yes\nSum = {sum_even}")
else:
    print(f"No\nDiff = {abs(sum_even - sum_odd)}")