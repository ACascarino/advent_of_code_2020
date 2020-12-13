with open("day06/input.txt", "r") as f:
    groups = [set(x.replace('\n', '')) for x in f.read().split("\n\n")]

group_size_sum = sum(map(len, groups))
print(group_size_sum)