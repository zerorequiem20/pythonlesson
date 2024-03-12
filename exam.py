marks = int(input("Enter the exam mark (between 1 and 100): "))

if 1 <= marks <= 100:
    if marks < 50:
        grade = 'Fail'
    elif 50 <= marks <= 60:
        grade = 'Pass'
    elif 61 <= marks <= 70:
        grade = 'Merit'
    elif 71 <= marks <= 100:
        grade = 'Distinction'

    print(f"The student's grade is: {grade}")

else:
    print("Invalid input: Marks must be between 1 and 100.")
