start_letter = ord("A")
end_letter = ord(input())
rows_first_sector = int(input())
seats_odd_row = int(input())

#small_letter = ord("a")
counter = 0
for sector in range(start_letter, end_letter + 1):
    for row in range(1, rows_first_sector + 1):
        small_letter = int(ord("a"))
        if row % 2 == 0:
            row_seats = seats_odd_row + 2
        else:
            row_seats = seats_odd_row

        for seat in range(small_letter, small_letter + row_seats):
            print(f"{chr(sector)}{row}{chr(seat)}")
            counter += 1
    rows_first_sector += 1
print(counter)