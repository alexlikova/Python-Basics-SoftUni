first_number = int(input())
second_number = int(input())

for number in range(first_number, second_number + 1):
    number_as_string = str(number)
    sum_even_position = 0 # вътре в цикъла е, за да може при всяко завъртане,
    sum_odd_position = 0 # на всяко различно число да ни брои четните и нечетните позиции сбора
    for index, digit in enumerate(number_as_string):
        if index % 2 == 0:
            sum_odd_position += int(digit)
        else:
            sum_even_position += int(digit)

    if sum_odd_position == sum_even_position:
        print(f"{number}", end=" ")