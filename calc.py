
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("\nCalculator Menu:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
print("5. Square (s)")

operation_choice = input("Choose an operation (1-5): ")

if operation_choice == '1':
    result = num1 + num2
    print(f"The sum of {num1} and {num2} is: {result}")
elif operation_choice == '2':
    result = num1 - num2
    print(f"The difference of {num1} and {num2} is: {result}")
elif operation_choice == '3':
    result = num1 * num2
    print(f"The product of {num1} and {num2} is: {result}")
elif operation_choice == '4':
    if num2 != 0: 
        result = num1 / num2
        print(f"The quotient of {num1} divided by {num2} is: {result}")
    else:
        print("Error: Cannot divide by zero.")
elif operation_choice == '5':
    result1 = num1 ** 2
    result2 = num2 ** 2
    print(f"The square of {num1} is: {result1}")
    print(f"The square of {num2} is: {result2}")
else:
    print("Invalid choice. Please choose a number between 1 and 5.")
