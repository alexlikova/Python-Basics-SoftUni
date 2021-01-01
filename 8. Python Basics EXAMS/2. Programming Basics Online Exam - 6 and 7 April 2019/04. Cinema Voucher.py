voucher_amount = int(input())

count_movie_tickets = 0
count_other = 0
sum_total = 0

command = input()
while command != "End":
    if len(command) > 8:
        length = 2
    else:
        length = 1
    for letter in command[0:length]:
        sum_total += ord(letter)

    if voucher_amount < sum_total:
        break
    elif length == 2:
        count_movie_tickets += 1
    else:
        count_other += 1

    command = input()

print(f"{count_movie_tickets}\n{count_other}")
