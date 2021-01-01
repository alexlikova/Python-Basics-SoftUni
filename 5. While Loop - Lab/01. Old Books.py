book_name = input()
book = input()

count_books = 0
while book != "No More Books":
    count_books += 1
    if book == book_name:
        print(f"You checked {count_books - 1} books and found it.")
        break
    book = input()

else:
    print(f"The book you search is not here!\nYou checked {count_books} books.")

#"""
book_name = input()

book_count = 0
is_book_found = False

current_book = input()

while current_book != "No More Books":
    if current_book == book_name:
        is_book_found = True
        break

    book_count += 1
    current_book = input()

if is_book_found:
    print(f"You checked {count_books} books and found it.")
else:
    print(f"The book you search is not here!\nYou checked {count_books} books.")

#"""