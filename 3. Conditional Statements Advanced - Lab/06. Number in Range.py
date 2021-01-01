"""
number = int (input())

for i in range (-100, 100):
    if (number != 0):
        print ("Yes")
    else:
        print ("No")
"""

number = int(input())

if -100 <= number <= 100 and number != 0:
    print("Yes")
else:
    print("No")