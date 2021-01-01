budget = float(input())
season = str(input()).lower()

expenses = 0.0
place_to_stay = ""

if (0 < budget <= 100 ):
    destination = "Bulgaria"
    if season == "summer":
        expenses = budget * 0.3
        place_to_stay = "Camp"
    elif season == "winter":
        expenses = budget * 0.7
        place_to_stay = "Hotel"
    else:
        print("Wrong season - choose between Summer or Winter")
elif (100 < budget <= 1000):
    destination = "Balkans"
    if season == "summer":
        expenses = budget * 0.4
        place_to_stay = "Camp"
    elif season == "winter":
        expenses = budget * 0.8
        place_to_stay = "Hotel"
    else:
        print("Wrong season - choose between Summer or Winter")
elif (budget > 1000):
    destination = "Europe"
    expenses = budget * 0.9
    place_to_stay = "Hotel"

print(f"Somewhere in {destination}\n{place_to_stay} - {expenses:.2f}")