
def animal (i):
    switcher = {
    "dog": "mammal",
    "crocodile": "reptile",
    "snake": "reptile",
    "tortoise" : "reptile"
    }
    return switcher.get(i, "unknown")

input = str(input().lower())

type_animal = animal(input)
print(type_animal)


