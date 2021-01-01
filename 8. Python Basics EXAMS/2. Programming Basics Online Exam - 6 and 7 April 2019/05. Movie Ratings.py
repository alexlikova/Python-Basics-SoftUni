import sys

number_of_movies = int(input())

heights_rating = - sys.maxsize
lowest_rating = sys.maxsize
heights_movie_rating = ""
lowest_movie_rating = ""
sum_rating = 0

for number in range(1, number_of_movies + 1):
    movie_name = input()
    rating = float(input())
    sum_rating += rating

    if rating > heights_rating:
        heights_rating = rating
        heights_movie_rating = movie_name
    elif rating < lowest_rating:
        lowest_rating = rating
        lowest_movie_rating = movie_name

print(f"{heights_movie_rating} is with highest rating: {heights_rating:.1f}")
print(f"{lowest_movie_rating} is with lowest rating: {lowest_rating}")
print(f"Average rating: {sum_rating / number_of_movies:.1f}")
