start_letter, end_letter, miss_letter = [ord(input()) for _ in range(3)]
count = 0
for start in range(start_letter, end_letter + 1):
    for middle in range(start_letter,end_letter + 1):
        for end in range(start_letter, end_letter + 1):
            if start != miss_letter and middle != miss_letter and end != miss_letter:
                print(f"{chr(start)}{chr(middle)}{chr(end)}", end=" ")
                count += 1

print(f"{count}")