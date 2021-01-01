"""
def maxlist(list):
    maxv = list[0]
    for x in list:
        maxv=max(maxv, x)
    return maxv;
"""

number_of_pairs = int(input())

list = []
sum_previous = 0

for pairs in range(number_of_pairs):
    for numbers in range(1, 3):
        number = int(input())
        sum_previous += number
    list.append(sum_previous)
    sum_previous = 0

# Using all()method - The all() method applies the comparison for each element in the list.
result = all(element == list[0] for element in list)

# Result from count matches with result from len() OR
#result = list.count(list[0]) == len(list)

if (result):
   print(f"Yes, value={list[0]}")       #All the elements are Equal
else:
    diff_list = []
    for i in range(1, len(list)):
        x = list[i] - list[i - 1]
        diff_list.append(x)
    print(f"No, maxdiff={max(diff_list)}")       #All Elements are not equal

