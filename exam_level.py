marks = int(input("Enter the exam mark (between 1 and 100): "))

student_level = int(input("Enter the student level (1 or 2): "))

if 1 <= marks <= 100:

    if student_level == 1:
        if marks < 50:
            grade = 'Fail'
        elif 50 <= marks <= 60:
            grade = 'Pass'
        elif 61 <= marks <= 70:
            grade = 'Merit'
        elif 71 <= marks <= 100:
            grade = 'Distinction'
    elif student_level == 2:
        if marks < 40:
            grade = 'Fail'
        elif 40 <= marks <= 50:
            grade = 'Pass'
        elif 51 <= marks <= 65:
            grade = 'Merit'
        elif 66 <= marks <= 100:
            grade = 'Distinction'
    else:
        grade = 'Error: Invalid student level. Please enter 1 or 2.'

    print(f"The student's grade is: {grade}")

else:
    print("Error: Marks must be between 1 and 100.")
