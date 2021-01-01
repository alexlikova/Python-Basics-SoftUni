"""
fruit = str(input()).lower()
day = str(input()).lower()
quality = float(input())

price = 0.0


def week_day_price(i):
    switcher = {
        "banana": 2.50, "apple": 1.20, "orange": 0.85, "grapefruit": 1.45, "kiwi": 2.70, "pineapple": 5.50,
        "grapes": 3.85
    }
    return switcher.get(i, "error")


def weekend_price(x):
    switcher = {
        "banana": 2.70, "apple": 1.25, "orange": 0.90, "grapefruit": 1.60, "kiwi": 3.00, "pineapple": 5.60,
        "grapes": 4.20
    }
    return switcher.get(x, "error")


if (day == "monday" or day == "tuesday" or day == "wednesday" or day == "thursday" or day == "friday"):
    find_price = week_day_price(fruit)
    new_price = float(find_price)
    price = new_price * quality

elif (day == "saturday" or "sunday"):
    find_price = weekend_price(fruit)
    price = quality * float(find_price)
else:
    print("error")

    print(price)
"""

weekday_fruit_price = {"banana": 2.50, "apple": 1.20, "orange": 0.85, "grapefruit": 1.45, "kiwi": 2.70,
                       "pineapple": 5.50, "grapes": 3.85}
weekend_fruit_price = {"banana": 2.70, "apple": 1.25, "orange": 0.90, "grapefruit": 1.60, "kiwi": 3.00,
                       "pineapple": 5.60, "grapes": 4.20}


def buyfruit(fruit, day):
    fruit_prices = {};
    if day == "monday" or day == "tuesday" or day == "wednesday" or day == "thursday" or day == "friday":
        fruit_prices = weekday_fruit_price;
    elif day == "saturday" or day == "sunday":
        fruit_prices = weekend_fruit_price;
    else:
        raise ValueError("error") #Day is invalid
    if fruit not in fruit_prices:
        raise ValueError("error"); #Fruit is invalid
    else:
        return fruit_prices[fruit]


text = str(input()).lower()
day = str(input()).lower()
quantity = float(input())
cost = 0.0

try:
    price = buyfruit(text, day)
    cost = price * quantity
    print(f"{cost:.2f}");
except ValueError as e:
    print(e)
