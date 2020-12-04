import numpy as np

with open("input.txt", "r") as f:
    input_list = tuple(map(float, f.readlines()))

small_list = iter(sorted(input_list))
large_list = iter(sorted(input_list, reverse=True))

small_elem = next(small_list)
large_elem = next(large_list)

while True:
    sum_elem = small_elem + large_elem
    if sum_elem > 2020:
        large_elem = next(large_list)
    elif sum_elem < 2020:
        small_elem = next(small_list)
    else:
        target_pair = (small_elem, large_elem)
        break

print(np.prod(target_pair))