#from pyfiglet import figlet_format
#print(figlet_format('VLADI', font='standard')) #doh, standard, isometric1
import math

n = int(input())

# first row
print(f"{'*' * n * 2}{' ' * n}{'*' * n * 2}")

#Middle row
middle_row = math.floor((n - 1) / 2 - 1)

for row in range(0, n - 2):
    if row == middle_row:
        print(f"*{'/' * (2 * n - 2)}*{'|' * n}*{'/' * (2 * n - 2)}*")
    else:
        print(f"*{'/' * (2 * n - 2)}*{' ' * n}*{'/' * (2 * n - 2)}*")

#last row
print(f"{'*' * n * 2}{' ' * n}{'*' * n * 2}")


"""
n = int(input())

for rows in range(0, n - 1):
    print(f"{'*' * n * 2}{' ' * n}{'*' * n * 2}")
    #if 0 <= rows < n - 2:
        #print(f"*{'|' * (2 * n - 2)}*{' ' * n}*{'|' * (2 * n - 2)}*")
    for middle_rows in range(rows, n - 2):
        print(f"*{'|' * (2 * n - 2)}*{' ' * n}*{'|' * (2 * n - 2)}*")
        #if rows == (n - 1) / 2 - 1:
            #print(f"{'*' * n}{'|' * n}{'*' * n}")
    #print(f"{'*' * n}{' ' * n}{'*' * n}")
"""