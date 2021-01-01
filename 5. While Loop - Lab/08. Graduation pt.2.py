name = str(input())

sum_grade = 0
count = 0
count_bad_grade = 0
while count < 12:
    grade = float(input())
    if grade < 4:
        count_bad_grade += 1
        if count_bad_grade == 2:
            print(f"{name} has been excluded at {count} grade")
            break
    sum_grade += grade
    count += 1

if count_bad_grade != 2:
    average_grade = sum_grade / count
    print(f"{name} graduated. Average grade: {average_grade:.2f}")