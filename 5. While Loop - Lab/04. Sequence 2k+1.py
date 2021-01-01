n = int(input())

# дествието --> number * 2 + 1
# СТОП --> number > n
# ПРОДЪЛЖИ --> number <= n

number = 1
while number <= n:
    print(number)
    number = 2 * number + 1