import numpy as np

TARGET_FACTORS = 3

with open("day1/input.txt", "r") as f:
    input_list = sorted(map(float, f.readlines()))

indices = list(range(-1, TARGET_FACTORS-1))
moving_index = TARGET_FACTORS-1
number_of_resets = 0

while True:
    target_elems = [input_list[i] for i in indices]
    sum_elems = np.sum(target_elems)

    if sum_elems > 2020:
        indices[0] -= 1
    elif sum_elems < 2020:
        indices[moving_index] += 1
    else:
        break

    if input_list[indices[0]] is input_list[indices[moving_index]]:
        number_of_resets += 1
        indices = [-1] + [i+number_of_resets for i in range(0, TARGET_FACTORS-1)]

print(np.prod(target_elems))