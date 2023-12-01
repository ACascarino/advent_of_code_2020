with open('day10/input.txt', 'r') as f:
    adaptors = sorted([int(x.rstrip('\n')) for x in f])

adaptors = [0] + adaptors + [max(adaptors) + 3]

joltages = []
for i in range(len(adaptors) - 1):
    joltages.append(abs(adaptors[i] - adaptors[i+1]))
print(joltages.count(1) * joltages.count(3))