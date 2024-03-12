print("Pythagoras' Calculator:")
print("1. Find the length of A given B and C")
print("2. Find the length of B given A and C")
print("3. Find the length of C given A and B")

choice = int(input("Enter your choice (1-3): "))

if choice == 1:
    B = float(input("Enter the length of B: "))
    C = float(input("Enter the length of C: "))
    A = (C**2) - (B**2)
    print(f"The length of A is: {A}")

elif choice == 2:
    A = float(input("Enter the length of A: "))
    C = float(input("Enter the length of C: "))
    B = (C**2) - (A**2)
    print(f"The length of B is: {B}")

elif choice == 3:
    A = float(input("Enter the length of A: "))
    B = float(input("Enter the length of B: "))
    C = (A**2) + (B**2)
    print(f"The length of C is: {C}")

else:
    print("Invalid choice. Please choose a number between 1 and 3.")
