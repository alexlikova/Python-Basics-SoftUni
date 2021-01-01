movie_name, category_hall, sold_tickets = input(), input(), int(input())

cinema = {
    "A Star Is Born": {"normal": 7.50, "luxury": 10.50, "ultra luxury": 13.50},
    "Bohemian Rhapsody": {"normal": 7.35, "luxury": 9.45, "ultra luxury": 12.75},
    "Green Book": {"normal": 8.15, "luxury": 10.25, "ultra luxury": 13.25},
    "The Favourite": {"normal": 8.75, "luxury": 11.55, "ultra luxury": 13.95}
}

revenue = cinema[movie_name][category_hall] * sold_tickets
print(f"{movie_name} -> {revenue:.2f} lv.")