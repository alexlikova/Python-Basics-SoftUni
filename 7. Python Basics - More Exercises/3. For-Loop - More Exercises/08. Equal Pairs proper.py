
number_of_pairs = int(input())
x, y = [int(input()) for _ in range (2)]
#y = int(input())
last_sum = x + y
max_diff = 0
all_same = True

pair = 2
while pair <= number_of_pairs:
    x = int(input())
    y = int(input())
    sum = x + y
    if sum != last_sum:
        all_same = False
    max_diff = max(max_diff, abs(sum - last_sum))
    last_sum = sum
    pair+=1

if all_same:
    print(f"Yes, value={last_sum}")
else:
    print(f"No, maxdiff={max_diff}")
