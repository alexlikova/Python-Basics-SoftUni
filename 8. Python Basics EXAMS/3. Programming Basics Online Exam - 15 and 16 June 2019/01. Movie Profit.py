movie_name = input()
days, total_tickets = int(input()), int(input())
price_ticket = float(input())
percent_for_the_cinema = int(input())

revenue_for_whole_period = days * total_tickets * price_ticket
cinema_revenue = (percent_for_the_cinema / 100) * revenue_for_whole_period
revenue_from_the_movie = revenue_for_whole_period - cinema_revenue
print(f"The profit from the movie {movie_name} is {revenue_from_the_movie:.2f} lv.")