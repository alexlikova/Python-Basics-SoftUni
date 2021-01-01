number = int(input())

sum_data = 0

while number > sum_data:
    data = int(input())
    sum_data += data
    if number <= sum_data:
        print(sum_data)
