#n, m = [int(input()) for _ in range(2)]

"""is_mach = False

for x1 in range(-n, n + 1):
    for y1 in range(-n, n + 1):
        for x2 in range(x1 + 1, n + 1):
            for y2 in range(y1 + 1, n + 1):
                #if not (-n <= x1 < x2 or -n <= y1 < y2 <= n):
                    #continue
                area = (x2 - x1) * (y2 - y1)
                if area >= m:
                   print(f'({x1}, {y1}) ({x2}, {y2}) -> {area}')
                   is_mach = True

if not is_mach:
    print('No')"""

n, m = [int(input()) for _ in range(2)]

count = 0

for left in range(-n, n):
    for top in range(-n, n):
        for right in range(left + 1, n + 1):
            for bottom in range(top + 1, n + 1):
                area = abs(right - left) * abs(bottom - top)

                if area >= m:
                    print('(%d, %d) (%d, %d) -> %d'
                          % (left, top, right, bottom, area))
                    count += 1
if count == 0:
    print(f"No")