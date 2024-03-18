import random

def roll_dice(num_dice):
    return [random.randint(1, 6) for _ in range(num_dice)]

def write_to_file(filename, data):
    with open(filename, 'w') as file:
        for item in data:
            file.write(str(item) + '\n')


roll1 = roll_dice(1)
write_to_file("file1.txt", roll1)
print("Roll 1:", roll1)

roll2 = roll_dice(2)
write_to_file("file2.txt", roll2)
print("Roll 2:", roll2)


