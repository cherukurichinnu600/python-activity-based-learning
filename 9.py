marks = []

n = int(input("Enter number of students: "))

for i in range(n):
    student = []
    print("Enter marks for student", i + 1)

    for j in range(3):
        m = int(input("Enter subject marks: "))
        student.append(m)

    marks.append(student)

for i in range(n):
    total = sum(marks[i])
    average = total / 3

    print("\nStudent", i + 1)
    print("Marks:", marks[i])
    print("Total:", total)
    print("Average:", average)
    