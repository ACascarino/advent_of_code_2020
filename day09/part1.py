BUFFER_SIZE = 25

with open("day09/input.txt", "r") as f:
    sequence = [int(x[:-1]) for x in f.readlines()]

i = BUFFER_SIZE
i_low = -BUFFER_SIZE - 1
i_high = -2
pres = sorted(sequence[i - BUFFER_SIZE:i + 1])
target = sequence[i]

while True:
    val_low = pres[i_low]
    val_high = pres[i_high]

    if i_low == i_high:
        break
    elif val_low + val_high > target:
        i_high -= 1
    elif val_low + val_high < target:
        i_low += 1
    elif val_low + val_high == target:
        i += 1
        i_low = -BUFFER_SIZE - 1
        i_high = -2
        pres = sorted(sequence[i - BUFFER_SIZE:i + 1])
        target = sequence[i]

print(target)