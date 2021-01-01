number_one_lv, number_two_lv, number_five_lv, money = [int(input()) for _ in range(4)]

for first in range(0, number_one_lv + 1):
    for second in range(0, number_two_lv + 1):
        for third in range(0, number_five_lv + 1):
            total = first * 1 + second * 2 + third * 5
            if money == total:
                print(f"{first} * 1 lv. + {second} * 2 lv. + {third} * 5 lv. = {money} lv.")
