type = input().lower()
rows = int(input())
columns = int(input())

ticket = 0.0
income = 0.0

if type == "premiere":
    ticket = 12.00
elif type == "normal":
    ticket = 7.50
elif type == "discount":
    ticket = 5.00

income = ticket * rows * columns

print(f"{income:.2f} leva")

