def display_lines(style):
    global i
    for i in range(11):
        print(f'{style * i:<1}', end="")


display_lines(">")
print()
print('{:>45s}'.format("welcome to school of hard-knocks".upper()))
display_lines("<")
print()

student_num = int(input("Enter number of Students: "))
course_num = int(input("Enter number of Subjects: "))
print()
lst_of_students_names = [input(f"Enter name of Student {x + 1}: ").title() for x in range(student_num)]
print()
print("Enter the student(s) subject scores".upper())
lst_of_courses = [input(f"Enter name of Subject {t + 1}: ").upper() for t in range(course_num)]
print()
students_records = []

for s in range(student_num):
    students_records.append([])
    for y in range(course_num):
        students_records[s].append(int(input(f"Enter {lst_of_students_names[s]}'s "
                                             f"score in {lst_of_courses[y].title()}: ")))
    print()


def calculate_students_results(lst_scores):
    sum_of_scores = []
    sum_item = 0
    for p in range(len(lst_scores)):
        for j in range(len(lst_scores[p])):
            sum_item += lst_scores[p][j]
        sum_of_scores.append(sum_item)
        sum_item = 0

    return sum_of_scores


print(f"{'STUDENT(S) GRADE REPORT SHEET':^60s}")

display_lines("|")
print()
print(f"{'STUDENT':>10}", end="")
print(f"{' '.join(['{:>7s}'.format(x) for x in lst_of_courses]):>8}", end="")
print(f"{'TOTAL':>10} {'POS':>6}")
display_lines("|")
print()

for i in range(len(lst_of_students_names)):
    print('{:>7s} {:>6d} {:>7d} {:>8d}'.format(lst_of_students_names[i].title(), *students_records[i],
                                               calculate_students_results(students_records)[i]))

print(calculate_students_results(students_records))

# print(students_records[i], end="")
# print(calculate_results(students_records, lst_of_students_names))

# print(enter_students_details())

# def sum_student_scores(lst, index) -> int:
#     sum_ = 0
#     for sum_scores in lst[index]:
#         sum_ += sum_scores
#     return sum_
#
#
# avg = sum_student_scores(students_records, 0) / len(students_records[0])


# print("Students list", lst_of_students_names)
# print("Course list", lst_of_courses)
# print("Scores of students", students_records)
# print(sum_student_scores(students_records, 0))


# lst_of_students_names = [input(f"Enter name of student {i + 1}: ") for i in range(0, student_num)]
# matrix = [[j for j in range(5)] for i in range(5)]
# matrix = [[j for j in range(course_num) if students_records[y]
#     .append(int(input(f"Enter {lst_of_students_names[y]} "
#                       f"score for {lst_of_courses[j]}: ")))] for y in range(student_num)]

# lst_of_courses = [input(f"Enter name of subject {i + 1}: ") for i in range(0, course_num)]
# students_records = [input(f"Enter scores of {i + 1}: ") for i in range(0, student_num)]
