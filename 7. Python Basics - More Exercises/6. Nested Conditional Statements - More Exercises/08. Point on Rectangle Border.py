x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x = float(input())
y = float(input())

fist_condition = bool((x == x1 or x == x2) and (y >= y1 and y <= y2))
second_condition = bool((y == y1 or y == y2) and (x >= x1 and x <= x2))

if fist_condition or second_condition:
    print("Border")
else:
    print("Inside / Outside")
