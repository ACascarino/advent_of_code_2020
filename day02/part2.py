with open("day02/input.txt", "r") as f:
    input_file = [tuple(l.split()) for l in f]

counter = 0
for schema, letter, password in input_file:
    first_position, second_position = [int(bound) - 1 for bound in schema.split('-')]

    if (password[first_position] == letter[0]) ^ (password[second_position] == letter[0]):
        counter += 1

print(counter) 
