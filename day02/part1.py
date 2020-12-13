with open("day02/input.txt", "r") as f:
    input_file = [tuple(l.split()) for l in f.readlines()]

counter = 0

for entry in input_file:
    schema, letter, password = entry
    lowbound, highbound = schema.split('-')
    letter = letter[0]
    
    occurances = password.count(letter)
    if int(lowbound) <= occurances and occurances <= int(highbound):
        counter += 1

print(counter)