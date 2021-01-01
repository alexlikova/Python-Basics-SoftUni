men, women, tables = [int(input()) for _ in range(3)]
count = 1
if 1 <= men <= 100 and 1 <= men <= 100 and 1 <= tables <= 100:
    for man in range(1, men + 1):
        for woman in range(1, women + 1):
            if count <= tables:
                print(f"({man} <-> {woman})", end=" ")
                count += 1
