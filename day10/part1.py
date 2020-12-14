import numpy as np

with open('day10/input.txt', 'r') as f:
    adaptors = sorted([int(x.rstrip('\n')) for x in f])

adaptors = [0] + adaptors + [max(adaptors) + 3]

joltages = list(np.diff(adaptors))
print(joltages.count(1) * joltages.count(3))