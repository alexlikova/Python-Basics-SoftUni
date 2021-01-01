import sys

count = 0
max_sum = - sys.maxsize
total_points_word = 0
movie_name_winner = ""
command = input()
while command != "STOP":
    movie_name = command

    for letter in movie_name:
        if 65 <= ord(letter) <= 90: # A, B, C, D, E, F, etc.
            points = ord(letter) - len(movie_name)
        elif 97 <= ord(letter) <= 122: # a, b, c, d, e, f, etc.
            points = ord(letter) - (len(movie_name) * 2)
        else:
            points = ord(letter)
        total_points_word += points
    count += 1
    if total_points_word > max_sum:
        max_sum = total_points_word
        movie_name_winner = movie_name
    total_points_word = 0
    if count == 7:
        print(f"The limit is reached.")
        break
    command = input()
print(f"The best movie for you is {movie_name_winner} with {max_sum} ASCII sum.")

"""
movie_name = ''
total = -10000
subtotal = 0
counter = 0
current_move = input()

while True:
    if current_move == 'STOP': break
    counter += 1
    if counter == 7: break

    for letter in current_move:
        if letter.isupper():
            subtotal += ord(letter) - len(current_move)
        elif letter.islower():
            subtotal += ord(letter) - len(current_move) * 2
        else:
            subtotal += ord(letter)
    if total < subtotal:
        total = subtotal
        movie_name = current_move
    subtotal = 0

    current_move = input()


if counter == 7:
    print('The limit is reached.')
print(f'The best movie for you is {movie_name} with {total} ASCII sum.')
"""