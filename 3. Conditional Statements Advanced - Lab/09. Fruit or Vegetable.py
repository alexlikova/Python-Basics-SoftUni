fruit = "fruit"
veg = "vegetable"

def choose(i):

    switcher = {
        "banana": fruit, "apple": fruit, "kiwi": fruit, "cherry": fruit, "lemon": fruit, "grapes": fruit,
        "tomato": veg, "cucumber": veg, "pepper": veg, "carrot": veg
    }
    return switcher.get(i, "unknown")

input = str(input()).lower()
what_choose = choose(input)
print(what_choose)