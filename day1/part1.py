import numpy as np

with open("input.txt", "r") as f:
    input_list = sorted(map(float, f.readlines()))

small_index = 0
large_index = -1

while True:
    sum_elem = input_list[small_index] + input_list[large_index]
    if sum_elem > 2020:
        large_index -= 1
    elif sum_elem < 2020:
        small_index += 1
    else:
        target_pair = (input_list[small_index], input_list[large_index])
        break

print(np.prod(target_pair))