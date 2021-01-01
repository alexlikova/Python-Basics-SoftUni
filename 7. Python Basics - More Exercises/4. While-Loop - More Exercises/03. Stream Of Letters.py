letter = input().title()

n_appeared, c_appeared, o_appeared = False
collection_of_words = ""
new_word = ""

while letter != "End":
    # letter from A-Z --> 65 do 90 vkl
    #first_condition = letter.isascii()
    # letter from a-z --> 97 do 122 vkl
    #second_condition =

    #if first_condition or second_condition:
    if letter.isalpha():
        if n_appeared:
            new_word += letter
            n_appeared = True
        elif c_appeared:
            new_word += letter
            c_appeared = True
        elif o_appeared:
            new_word += letter
            o_appeared = True
        else:
            new_word += letter

    if n_appeared and c_appeared and o_appeared:
        collection_of_words += new_word + " "
        n_appeared = False
        c_appeared = False
        o_appeared = False

    letter = input().title()

print(collection_of_words)

"""

chars = input()
word_collection = ''
word = ''
c, o, n = False, False, False

while chars != 'End':
    if chars.isalpha():
       if (chars =='c' and c != True) or (chars =='o' and o != True) or (chars =='n' and n != True):
            if chars =='c': c = True
            if chars =='o': o = True
            if chars =='n': n = True
       else:
          word += chars

    if c and o and n:
       word_collection += word + ' '
       c, o, n = False, False, False
       word = ''

    chars =  input()

print(word_collection)
"""