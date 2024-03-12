names_list = []

for i in range(5):
    name = input(f"Enter name {i + 1}: ")
    names_list.append(name)

for name in names_list:
    print(name,"is a great name")

''' using list comp

names_list = [input(f"Enter name {i + 1}: ") for i in range(5)]

[print(name,"is a great name") for name in names_list]
'''
