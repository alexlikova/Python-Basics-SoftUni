upper_hundreds, upper_tens, upper_units = [int(input()) for _ in range(3)]

for hundreds in range(1, upper_hundreds + 1):
    for tens in range(1, upper_tens + 1):
        for units in range(1, upper_units + 1):
            if hundreds % 2 == 0 and units % 2 == 0:
                if tens == 2 or tens == 3 or tens == 5 or tens == 7:
                    print(f"{hundreds} {tens} {units}")
