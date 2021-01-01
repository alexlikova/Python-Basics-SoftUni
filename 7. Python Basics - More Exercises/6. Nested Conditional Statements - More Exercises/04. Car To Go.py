budget = float(input())
season = input()

class_car = ""
type_car = ""

if 0 < budget <= 100:
    class_car = "Economy class"
    if season == "Summer":
        type_car = "Cabrio"
        budget *= 0.35
    elif season == "Winter":
        type_car = "Jeep"
        budget *= 0.65
    else:
        print(input("Wrong season. Choose between Summer or Winter: "))
elif 100 < budget <= 500:
    class_car = "Compact class"
    if season == "Summer":
        type_car = "Cabrio"
        budget *= 0.45
    elif season == "Winter":
        type_car = "Jeep"
        budget *= 0.80
    else:
        print(input("Wrong season. Choose between Summer or Winter: "))

elif budget > 500:
    class_car = "Luxury class"
    type_car = "Jeep"
    budget *= 0.9

else:
    print(input("Error, budget cannot be negative number. Try again: "))

print(f"{class_car}\n{type_car} - {budget:.2f}")