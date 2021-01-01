number_one = int(input())
number_two = int(input())
operator = str(input())

result = 0.0
what = ""

if (operator == "+"):
    result = number_one + number_two

    if result % 2 == 0:
        what = "even"
    else:
        what = "odd"

    print(f"{number_one} {operator} {number_two} = {result:.0f} - {what}")
elif operator == "-":
    result = number_one - number_two
    if result % 2 == 0:
        what = "even"
    else:
        what = "odd"

    print(f"{number_one} {operator} {number_two} = {result:.0f} - {what}")
elif operator == "*":
    result = number_one * number_two
    if result % 2 == 0:
        what = "even"
    else:
        what = "odd"

    print(f"{number_one} {operator} {number_two} = {result:.0f} - {what}")

elif operator == "%":
    if number_two == 0:
        print(f"Cannot divide {number_one} by zero")
    else:
        result = number_one % number_two
        print(f"{number_one} {operator} {number_two} = {result:.0f}")

elif operator == "/" and number_two != 0:
    result = number_one / number_two
    print(f"{number_one} {operator} {number_two} = {result:.2f}")
elif operator == "/" and number_two == 0:
    print(f"Cannot divide {number_one} by zero")

"""
n_one, n_two, operator = int(input()), int(input()), input()
try:
    result = eval(f'n_one  {operator}  n_two')
    if operator == '+' or operator == '-' or operator == '*':
        is_even  = 'even' if result % 2 == 0 else 'odd'
        print(f'{n_one} {operator} {n_two} = {result} - {is_even}')
    elif operator == '/':
        print(f'{n_one} {operator} {n_two} = {result:.2f}')
    else:
        print(f'{n_one} {operator} {n_two} = {result}')
except:
    print(f'Cannot divide {n_one} by zero')
"""