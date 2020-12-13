with open("day6/input.txt", "r") as f:
    groups = [x.split('\n') for x in f.read().split('\n\n')]

total_length = 0
for group in groups:
    individuals = tuple(map(set, group))
    total_length += len(individuals[0].intersection(*individuals))

print(total_length)

