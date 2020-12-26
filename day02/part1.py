with open("day02/input.txt", "r") as f:
    input_file = [tuple(l.split()) for l in f.readlines()]

counter = 0

for entry in input_file:
    schema, letter, password = entry
    lowbound, highbound = schema.split('-')
    
    occurances = password.count(letter[0])
    if int(lowbound) <= occurances <= int(highbound):
        counter += 1

print(counter)
