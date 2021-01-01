budget = float(input())
destination = input()
season = input()
days = int(input())

movie_destination = {
    "Dubai": {"Winter": 45_000, "Summer": 40_000},
    "Sofia": {"Winter": 17_000, "Summer": 12_500},
    "London": {"Winter": 24_000, "Summer": 20_250},
}

price = movie_destination[destination][season] * days

if destination == "Dubai":
    price *= 0.7
elif destination == "Sofia":
    price *= 1.25

diff = abs(budget - price)

if budget >= price:
    print(f"The budget for the movie is enough! We have {diff:.2f} leva left!")
else:
    print(f"The director needs {diff:.2f} leva more!")
