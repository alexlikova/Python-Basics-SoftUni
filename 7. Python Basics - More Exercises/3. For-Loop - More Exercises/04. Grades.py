
students_count = int(input())
grades = [float(input()) for _ in range(students_count)]

def calc_grades(*args):
    test = ''
    if args[0] == 5:
        test = lambda x: x >= args[0]
    elif args[0] == 4:
        test = lambda x: args[0] <= x <= args[1]
    elif args[0] == 3:
        test = lambda x: args[0] <= x <= args[1]
    elif args[0] < 3:
        test = lambda x: args[0] > x

    return f'{len(list(filter(test, grades))) / students_count * 100:.2f}%'


print(f'Top students: {calc_grades(5)}')
print(f'Between 4.00 and 4.99: {calc_grades(4, 4.99)}')
print(f'Between 3.00 and 3.99: {calc_grades(3, 3.99)}')
print(f'Fail: {calc_grades(2.99)}')
print(f'Average: {sum(grades) / students_count:.2f}')


"""
number_of_students = int(input())

total_sum_grades = 0
students = {"top students": 0, "good_veryGood students": 0, "average_good students": 0, "fail students": 0}

for student in range(number_of_students):
    grade = float(input())

    if 2.00 <= grade <= 2.99:
        students["fail students"] += 1
    elif 3.00 <= grade <= 3.99:
        students["average_good students"] += 1
    elif 4.00 <= grade <= 4.99:
        students["good_veryGood students"] += 1
    elif 5.00 <= grade <= 6.00:
        students["top students"] += 1
    else:
        print("Error, needs to be: 2.00 <= positive number <= 6.00: ")
    total_sum_grades += grade

average_grade = total_sum_grades / number_of_students
top_students = students["top students"] / number_of_students * 100
good_veryGood_students = students["good_veryGood students"] / number_of_students * 100
average_good_students = students["average_good students"] / number_of_students * 100
fail_students = students["fail students"] / number_of_students * 100

print(f"Top students: {top_students:.2f}%\nBetween 4.00 and 4.99: {good_veryGood_students:.2f}%\n"
      f"Between 3.00 and 3.99: {average_good_students:.2f}%\nFail: {fail_students:.2f}%\nAverage: {average_grade:.2f}")

"""