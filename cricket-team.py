def write_teams_to_file(filename):
  with open(filename, 'w') as file:
      file.write("India\n")
      file.write("Australia\n")
      file.write("England\n")
      file.write("South Africa\n")
      file.write("New Zealand\n")

def read_and_edit_file(filename):
  with open(filename, 'r+') as file:
      teams = file.readlines()
      first_team = teams[0].strip()
      fourth_team = teams[3].strip()

      # Edit the first line
      file.seek(0)
      file.write("this is a new line\n")

  return first_team, fourth_team

def main():
  filename = "teams.txt"
  write_teams_to_file(filename)

  first_team, fourth_team = read_and_edit_file(filename)

  print("First cricket team:", first_team)
  print("Fourth cricket team:", fourth_team)

  print("\nEdited File:")
  with open(filename, 'r') as file:
      for line in file:
          print(line.strip())

if __name__ == "__main__":
  main()
