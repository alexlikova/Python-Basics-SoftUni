import math
import sys

sugar = 950
flour = 750

amount_sugar = 0
amount_flour = 0
max_consumed_sugar = -sys.maxsize
max_consumed_flour = -sys.maxsize
easter_bread = int(input())
for number in range(1, easter_bread + 1):
    consumed_sugar = int(input())
    consumed_flour = int(input())

    amount_sugar += consumed_sugar
    amount_flour += consumed_flour

    if consumed_sugar > max_consumed_sugar:
        max_consumed_sugar = consumed_sugar
    if consumed_flour > max_consumed_flour:
        max_consumed_flour = consumed_flour

packages_sugar = math.ceil(amount_sugar / sugar)
packages_flour = math.ceil(amount_flour / flour)

print(f"Sugar: {packages_sugar}\nFlour: {packages_flour}\n"
      f"Max used flour is {max_consumed_flour} grams, "
      f"max used sugar is {max_consumed_sugar} grams.")