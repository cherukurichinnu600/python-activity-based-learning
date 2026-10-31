total_classes = int(input("Enter total classes: "))
attended = int(input("Enter attended classes: "))

percentage = (attended / total_classes) * 100

print("Attendance:", percentage, "%")

required = 75

if percentage >= required:
    print("You are eligible")
else:
    extra = 0
    while ((attended + extra) / (total_classes + extra)) * 100 < required:
        extra = extra + 1

    print("Extra classes required:", extra)