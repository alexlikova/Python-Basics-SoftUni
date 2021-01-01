movie_name = input()
package_type = input()
tickets = int(input())

movie_premiere = {
    "John Wick": {"Drink": 12.0, "Popcorn": 15, "Menu": 19},
    "Star Wars": {"Drink": 18, "Popcorn": 25, "Menu": 30},
    "Jumanji": {"Drink": 9, "Popcorn": 11, "Menu": 14}
}

price = movie_premiere[movie_name][package_type] * tickets

if movie_name == "Star Wars" and tickets >= 4:
    price *= 0.7
elif movie_name == "Jumanji" and tickets == 2:
    price *= 0.85

print(f"Your bill is {price:.2f} leva.")