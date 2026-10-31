attendance = int(input("Enter attendance percentage: "))
marks = int(input("Enter internal marks: "))
lab = input("Have you completed lab? (yes/no): ")
fees = input("Have you paid fees? (yes/no): ")

if attendance >= 75 and marks >= 20 and lab == "yes" and fees == "yes":
    print("Student is eligible for examination")
else:
    print("Student is not eligible")

    if attendance < 75:
        print("Attendance is insufficient")

    if marks < 20:
        print("Internal marks are insufficient")

    if lab != "yes":
        print("Lab work is incomplete")

    if fees != "yes":
        print("Fees are not paid")
        