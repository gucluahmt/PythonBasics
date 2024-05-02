with open('./../data/student_txt') as students:
    names = students.read()
    print(names)

with open('./../data/student_txt', 'a') as students:
    students.write("\nLionel Messi")
    print(students)

with open('./../data/student_txt') as students:
    names = students.read()
    print(students)