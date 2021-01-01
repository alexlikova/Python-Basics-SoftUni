command = input()

student_tickets = 0
kid_tickets = 0
standard_tickets = 0
sold_tickets = 0
total_sold_ticket = 0

while command != "Finish":

    movie_name = command
    free_spaces = int(input())

    for type_ticket in range(1, free_spaces + 1):
        type_ticket = input()
        if type_ticket == "standard":
            standard_tickets += 1
        elif type_ticket == "kid":
            kid_tickets += 1
        elif type_ticket == "student":
            student_tickets += 1
        elif type_ticket == "End":
            break
        sold_tickets += 1
    total_sold_ticket += sold_tickets
    print(f"{movie_name} - {sold_tickets / free_spaces * 100 :.2f}% full.")
    sold_tickets = 0
    command = input()

print(f"Total tickets: {total_sold_ticket}")
print(f"{student_tickets / total_sold_ticket * 100 :.2f}% student tickets.")
print(f"{standard_tickets / total_sold_ticket * 100 :.2f}% standard tickets.")
print(f"{kid_tickets / total_sold_ticket * 100 :.2f}% kids tickets.")
