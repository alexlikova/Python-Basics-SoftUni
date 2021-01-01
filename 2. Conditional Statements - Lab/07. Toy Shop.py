"""
travel = float(input())
puzzle = int(input())
dolls = int(input())
teddy_bears = int(input())
minions = int(input())
trucks = int(input())
"""

trip, puzzle, doll, bear, minion, truck = [float(input()) for _ in range(6)]

puzzle_price = 2.60
dolls_price = 3
teddy_bears_price = 4.1
minions_price = 8.2
trucks_price = 2

total_price = puzzle_price * puzzle + dolls_price * doll + teddy_bears_price * bear + minions_price * minion + trucks_price * truck

total_count = puzzle + doll + bear + minion + truck

if total_count >= 50:
    total_price *= 0.75

total_price *= 0.9

if total_price >= trip:
    print(f"Yes! {(total_price - trip):.2f} lv left.")
else:
    print(f"Not enough money! {(trip - total_price):.2f} lv needed.")