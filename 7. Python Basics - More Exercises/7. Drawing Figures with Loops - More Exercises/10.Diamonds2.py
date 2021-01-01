n = int(input())

leftRight = int((n - 1) / 2)
# 1st row
for i in range(1, leftRight + 1):
    print(f"{'-' * leftRight}*", end="")
    mid = n - 2 * leftRight - 2
    if mid >= 0:
        print(f"{'-' * mid}*", end="")

    print(f"{'-' * leftRight}")
    leftRight -= 1

# Bottom part
for i in range(1, int(((n+1)/2) + 1)):
    leftRight = i - 1
    mid = n - 2 * leftRight - 2
    print(f"{'-' * leftRight}*", end="")
    if mid >= 0:
        print(f"{'-' * mid}*", end="")
    print(f"{'-' * leftRight}")
