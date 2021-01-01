import math
import sys

max_score = - sys.maxsize
strongest_word = ""

# letters in vowel as a list
vowel = ["a", "e", "i", "o", "u", "y", "A", "E", "I", "O", "U", "Y"]

word = input()
while word != "End of words":
    current_score = 0
    for letter in word:
        current_score += ord(letter)

# convert your list to a tuple and pass it to startswith:
    if word.startswith(tuple(vowel)):
        current_score *= len(word)
    else:
        current_score = math.floor(current_score / len(word))

    if max_score <= current_score:
        max_score = current_score
        strongest_word = word
    word = input()

print(f"The most powerful word is {strongest_word} - {max_score}")
