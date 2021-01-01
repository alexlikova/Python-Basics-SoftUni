budget = float(input())
number_statists = int(input())
one_clothes = float(input())

decor = budget * 0.1;

if number_statists > 150:
    money_clothes = (one_clothes * number_statists) * 0.9
else:
    money_clothes = one_clothes * number_statists

leftMoney = budget - decor - money_clothes

if leftMoney >=0:
    print(f"Action!\n Wingard starts filming with {leftMoney:.2f} leva left.")
else:
    print(f"Not enough money! \nWingard needs {abs(leftMoney):.2f} leva more.")