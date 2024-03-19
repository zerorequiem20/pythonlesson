import re

class PasswordStrengthChecker:
  def __init__(self):
    self.password_history ={}

  def check_pass_strength(self,password):
    strength=0
    if len(password) >= 8:
      strength +=1

    if any(c.isupper() for c in password) and any(c.lower() for c in password):
      strength +=1
    
    if any(c.isdigit() for c in password):
      strength +=1

    if re.search(r'[!@#$%^&*()\-_=+{};:,<.>]', password):
      strength +=1

    if strength==1:
      return "weak"
    elif strength==2:
      return "medium"
    elif strength==3:
      return "strong"
    elif strength==4:
      return "very strong"
    else:
      return "very weak"

  def run(self):
    while True:
      password = input("Enter the password or enter exit to quit:  ")
      if password.lower() == "exit":
        break
      strength = self.check_pass_strength(password)
      print("Password strength: ", strength)
      self.password_history[password]= strength
      print(self.password_history)

if __name__ == "__main__":
  checker = PasswordStrengthChecker()
  checker.run()

