while True:
  try:
      choice = int(input("Enter a choice \n 1. Kgs to lbs \n 2. Lbs to kgs: "))

      if choice == 1:
          weightKg = float(input("Enter the weight in kgs: "))
          weightLbs = weightKg * 2.2
          print("The weight in lbs is", weightLbs)
          break  # Exit the loop if input is valid
      elif choice == 2:
          weightLbs = float(input("Enter the weight in lbs: "))
          weightKg = weightLbs / 2.2
          print("The weight in kgs is", weightKg)
          break  # Exit the loop if input is valid
      else:
          print("Invalid choice. Please enter 1 or 2.")

  except ValueError:
      print("Invalid input. Please enter a valid number.")
