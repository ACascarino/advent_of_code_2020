def recursive_function(index, sequence, cache):
    pool = []
    result = []

    if index == -len(sequence):
        return 1

    for i in range(max(index-3, -len(sequence)), index):
        if sequence[i] >= sequence[index] - 3:
            pool.append(i)
    for i in pool:
        cached_value = filter(lambda x: x[0] == i, cache)
        if (res := next(cached_value, None)) is not None:
            result.append(res[1])
        else:
            result.append(recursive_function(i, sequence, cache))

    cache.append((index, sum(result)))
    return(sum(result))


with open('day10/input.txt', 'r') as f:
    adaptors = sorted([int(x.rstrip('\n')) for x in f])

adaptors = [0] + adaptors + [max(adaptors) + 3]

cache = []
answer = recursive_function(-1, adaptors, cache)
print(answer)