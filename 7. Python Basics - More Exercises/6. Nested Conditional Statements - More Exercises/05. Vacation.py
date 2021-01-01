budget = float(input())
season = input()

place_sleep = ""
place_to_go = ""

if 0 < budget <= 1000:
    place_sleep = "Camp"
    if season == "Summer":
        place_to_go = "Alaska"
        budget *= 0.65
    elif season == "Winter":
        place_to_go = "Morocco"
        budget *= 0.45
    else:
        print(input("Wrong season. Choose between Summer or Winter: "))
elif 100 < budget <= 3000:
    place_sleep = "Hut"
    if season == "Summer":
        place_to_go = "Alaska"
        budget *= 0.80
    elif season == "Winter":
        place_to_go = "Morocco"
        budget *= 0.60
    else:
        print(input("Wrong season. Choose between Summer or Winter: "))

elif budget > 3000:
    place_sleep = "Hotel"
    if season == "Summer":
        place_to_go = "Alaska"
    elif season == "Winter":
        place_to_go = "Morocco"
    else:
        print(input("Wrong season. Choose between Summer or Winter: "))
    budget *= 0.9

else:
    print(input("Error, budget cannot be negative number. Try again: "))

print(f"{place_to_go} - {place_sleep} - {budget:.2f}")