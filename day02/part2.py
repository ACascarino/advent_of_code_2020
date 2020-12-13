with open("day02/input.txt", "r") as f:
    input_file = [tuple(l.split()) for l in f.readlines()]

counter = 0

for entry in input_file:
    schema, letter, password = entry

    first_position, second_position = schema.split('-')
    first_position = int(first_position) - 1
    second_position = int(second_position) - 1

    letter = letter[0]

    if bool(password[first_position] == letter) ^ bool(password[second_position] == letter):
        counter += 1

print(counter)