start = int(input())
end = int(input())

if 1 <= start <= 9 and 1 <= end <= 10:
    for a in range(start, end + 1):
        for b in range(start, end + 1):
            for c in range(start, end + 1):
                for d in range(start, end + 1):
                    if (a % 2 == 0 and d % 2 == 1) or (d % 2 == 0 and a % 2 == 1):
                        if a > d:
                            if (b + c) % 2 == 0:
                                print(f"{a}{b}{c}{d}", end=" ")
