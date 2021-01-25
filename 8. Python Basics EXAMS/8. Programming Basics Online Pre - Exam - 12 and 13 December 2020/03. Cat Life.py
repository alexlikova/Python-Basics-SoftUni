import math

breed_cat, sex_cat = [input() for _ in range(2)]

cat_breed = False

cat_breed_dict = {
    "m": {"British Shorthair": 13, "Siamese": 15, "Persian": 14, "Ragdoll": 16, "American Shorthair": 12, "Siberian": 11},
    "f": {"British Shorthair": 14, "Siamese": 16, "Persian": 15, "Ragdoll": 17, "American Shorthair": 13, "Siberian": 12}
}

if sex_cat in cat_breed_dict: # sex_cat == "m" or sex_cat == "f":
    if breed_cat in cat_breed_dict[sex_cat]:
        cat_life = (cat_breed_dict[sex_cat][breed_cat] * 12) / 6
        cat_breed = True
    else:
        cat_breed = False

if cat_breed:
    print(f"{math.floor(cat_life)} cat months")
else:
    print(f"{breed_cat} is invalid cat!")