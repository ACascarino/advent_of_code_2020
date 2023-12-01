def bin_str_to_int(value):
    return int(value, 2)

def int_str_to_bin_str(value, bits):
    return format(int(value), 'b').zfill(bits)

def apply_mask(mask, value):
    return "".join([value[i] if bit == "X" else bit for i, bit in enumerate(mask)])

with open("day14/input.txt", "r") as f:
    instructions = [line.rstrip("\n").split(" = ") for line in f]

memory = dict()
mask = "X"*36

for instruction in instructions:
    left, right = instruction
    if left == "mask":
        mask = right
    else:
        address = int(left[4:-1])
        bin_str = int_str_to_bin_str(right, bits=36)
        value = apply_mask(mask, bin_str)
        memory |= {address: bin_str_to_int(value)}

print(sum(memory.values()))