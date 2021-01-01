sum_non_prime_numbers = 0
sum_prime_numbers = 0

command = input().lower()
while command != "stop":
    number = int(command)

    if number < 0:
        print("Number is negative.")
        command = input()
        continue

    for i in range(2, number):
        if number % i == 0:
            sum_non_prime_numbers += number
            break
    else:
        sum_prime_numbers += number
    command = input().lower()

print(f"Sum of all prime numbers is: {sum_prime_numbers}")
print(f"Sum of all non prime numbers is: {sum_non_prime_numbers}")