key = ["A", "B", "C", "D", "A"]

answers = []

for i in range(5):
    ans = input("Enter answer for question " + str(i + 1) + ": ")
    answers.append(ans.upper())

correct = 0
wrong = 0
unanswered = 0

for i in range(5):
    if answers[i] == "":
        unanswered = unanswered + 1
    elif answers[i] == key[i]:
        correct = correct + 1
    else:
        wrong = wrong + 1

marks = correct * 2 - wrong * 0.5

print("Correct answers:", correct)
print("Wrong answers:", wrong)
print("Unanswered:", unanswered)
print("Total marks:", marks)
