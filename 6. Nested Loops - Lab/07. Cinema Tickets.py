command = input()

student_ticket = 0
standard_ticket = 0
kid_ticket = 0
total_tickets = 0
while command != "Finish":
    movie_name = str(command)
    free_space = int(input())
    sold_ticket = 0

    while movie_name != "End":
        ticket = input()
        if ticket == "student":
            student_ticket += 1
        elif ticket == "standard":
            standard_ticket += 1
        elif ticket == "kid":
            kid_ticket += 1
        total_tickets += 1
        sold_ticket += 1
        if sold_ticket >= free_space:
            break
        movie_name = input()
    print(f"{movie_name} - {total_tickets/free_space * 100:.2f}% full.")
    command = input()

print(f"Total tickets: {total_tickets}")
print(f"{student_ticket / total_tickets *100:.2f}%% student tickets.")
print(f"{standard_ticket / total_tickets *100:.2f}%% standard tickets.")
print(f"{kid_ticket / total_tickets *100:.2f}%% kids tickets.")
