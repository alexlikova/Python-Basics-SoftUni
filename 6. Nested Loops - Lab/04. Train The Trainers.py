number_of_jury = int(input())

total_sum = 0
total_number_grades = 0
command = input()
while command != "Finish":
    name_presentation = str(command)
    sum_grade = 0
    for grade_number in range(1, number_of_jury + 1):
        grade = float(input())
        sum_grade += grade
        total_sum += grade
        total_number_grades += 1
    print(f"{name_presentation} - {sum_grade/number_of_jury:.2f}.")
    command = input()

print(f"Student's final assessment is {total_sum/total_number_grades:.2f}.")
