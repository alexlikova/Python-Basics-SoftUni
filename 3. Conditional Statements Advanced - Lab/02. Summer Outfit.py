degrees = int(input())
time_of_the_day = input().lower()

outfit = ""
shoes = ""

if 10 <= degrees <= 18:
    if time_of_the_day == "morning":
        outfit = "Sweatshirt"
        shoes = "Sneakers"
    elif time_of_the_day == "afternoon":
        outfit = "Shirt"
        shoes = "Moccasins"
    elif time_of_the_day == "evening":
        outfit = "Shirt"
        shoes = "Moccasins"

elif 18 < degrees <= 24:
    if time_of_the_day == "morning":
        outfit = "Shirt"
        shoes = "Moccasins"
    elif time_of_the_day == "afternoon":
        outfit = "T-Shirt"
        shoes = "Sandals"
    elif time_of_the_day == "evening":
        outfit = "Shirt"
        shoes = "Moccasins"

elif (degrees >= 25):
    if time_of_the_day == "morning":
        outfit = "T-Shirt"
        shoes = "Sandals"
    elif time_of_the_day == "afternoon":
        outfit = "Swim Suit"
        shoes = "Barefoot"
    elif time_of_the_day == "evening":
        outfit = "Shirt"
        shoes = "Moccasins"

else:
    print("not valid input. Type number 10 or above")

print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")
