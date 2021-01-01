maximum_bad_grade = int(input())

total_score = 0
number_of_problems = 0
last_problem = ""
number_of_bad_grades = 0
too_many_bad_grades = False

command= input()

count = 0

while command != "Enough":
    last_problem = command
    current_grade = int(input())
    if current_grade <= 4:
        number_of_bad_grades += 1
        if maximum_bad_grade == number_of_bad_grades:
            too_many_bad_grades = True
            break
    number_of_problems += 1
    total_score += current_grade
    command= input()

if too_many_bad_grades:
    print(f"You need a break, {maximum_bad_grade} poor grades.")
else:
    average_score = total_score / number_of_problems
    print(f"Average score: {average_score:.2f}\nNumber of problems: {number_of_problems}\nLast problem: {last_problem}")