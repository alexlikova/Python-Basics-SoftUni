
"""
city = str(input()).lower()
volume_sales = float(input())

comission = -1.0

if (0 <= volume_sales <= 500):
    if (city == "sofia"):
        comission=0.05
    elif (city == "plovdiv"):
        comission = 0.055
    elif (city == "varna"):
        comission = 0.045

    money = comission * volume_sales
    print(f"{money:.2f}")

elif (500 < volume_sales <= 1000):
    if (city == "sofia"):
        comission=0.07
    elif (city == "plovdiv"):
        comission = 0.08
    elif (city == "varna"):
        comission = 0.075

    money = comission * volume_sales
    print(f"{money:.2f}")

elif (1000 < volume_sales <= 10000):
    if (city == "sofia"):
        comission = 0.08
    elif (city == "plovdiv"):
        comission = 0.12
    elif (city == "varna"):
        comission = 0.10

    money = comission * volume_sales
    print(f"{money:.2f}")

elif (volume_sales > 10000):
    if (city == "sofia"):
        comission = 0.12
    elif (city == "plovdiv"):
        comission = 0.145
    elif (city == "varna"):
        comission = 0.13

    money = comission * volume_sales
    print(f"{money:.2f}")

if (city != "plovdiv" or city != "sofia" or city != "varna" and volume_sales < 0):
        print("error")
else:
    print()
"""
"""

city = input()
money = float(input())
towns_list = ["Sofia", "Varna", "Plovdiv"]
result = 0

info_dict = {
    'Sofia': { 's': 5, 'm': 7, 'l': 8, 'xl': 12 },
    'Varna': { 's': 4.5, 'm': 7.5, 'l': 10, 'xl': 13 },
    'Plovdiv': { 's': 5.5, 'm': 8, 'l': 12, 'xl': 14.5 }
  }

if (city in towns_list) == False or (money < 0) == True:
    print("error")
    exit()

if money <= 500:
    result = (info_dict[city]['s'] * money) / 100
elif 500 < money <= 1000:
    result = (info_dict[city]['m'] * money) / 100
elif 1000 < money <= 10000:
   result = (info_dict[city]['l'] * money) / 100
elif money > 10000:
   result = (info_dict[city]['xl'] * money) / 100

print(f'{result:.2f}')
"""



city = str(input()).lower()
sales = float(input())

commission = -1.0

if city == "sofia":
    if 0 <= sales <= 500:
        commission = sales * 0.05
    elif 500 <sales <= 1000:
        commission = sales * 0.07
    elif 1000 < sales <= 10000:
        commission = sales * 0.08
    elif sales > 10000:
        commission = sales * 0.12
    else:
        print("error")
    com = sales * commission
    print(f"{commission:.2f}")

elif city == "varna":
    if 0 <= sales <= 500:
        commission = sales * 0.045
    elif 500 < sales <= 1000:
        commission = sales * 0.075
    elif 1000 < sales <= 10000:
        commission = sales * 0.10
    elif sales > 10000:
        commission = sales * 0.13
    else:
        print("error")
    print(f"{commission:.2f}")

elif city == "plovdiv":
    if 0 <= sales <= 500:
        commission = sales * 0.055
    elif 500 < sales <= 1000:
        commission = sales * 0.08
    elif 1000 < sales <= 10000:
        commission = sales * 0.12
    elif sales > 10000:
        commission = sales * 0.145
    else:
        print("error")
        exit()
    print(f"{commission:.2f}")

else:
    if sales <= 0 or city != "plovdiv" or city != "varna" or city != "sofia":
        print("error")
    else:
        print("error")

"""
city = input()
money = float(input())
result = 0

info_dict = {
    'Sofia': { 's': 5, 'm': 7, 'l': 8, 'xl': 12 },
    'Varna': { 's': 4.5, 'm': 7.5, 'l': 10, 'xl': 13 },
    'Plovdiv': { 's': 5.5, 'm': 8, 'l': 12, 'xl': 14.5 }
  }

if not city in info_dict or money < 0:
    print("error")
    exit()

if money <= 500:
    result = (info_dict[city]['s'] * money) / 100
elif 500 < money <= 1000:
    result = (info_dict[city]['m'] * money) / 100
elif 1000 < money <= 10000:
   result = (info_dict[city]['l'] * money) / 100
elif money > 10000:
   result = (info_dict[city]['xl'] * money) / 100

print(f'{result:.2f}')
"""