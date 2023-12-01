def bin_str_to_int(value):
    return int(value, 2)

def int_str_to_bin_str(value, bits):
    return format(int(value), 'b').zfill(bits)

def apply_mask(mask, value):
    masked_value = "".join([value[i] if bit == "0" else bit for i, bit in enumerate(mask)])

    xs = masked_value.count("X")
    inserts = [f"{i:0>{xs}b}" for i in range(2**xs)]
    value_template = masked_value.replace("X", "%s")
    values = [value_template % tuple(insert) for insert in inserts]
    return values

with open("day14/input.txt", "r") as f:
    instructions = [line.rstrip("\n").split(" = ") for line in f]

memory = dict()
mask = "0"*36

for left, right in instructions:
    if left == "mask":
        mask = right
    else:
        in_address = left.strip("mem[]")
        bin_str = int_str_to_bin_str(in_address, bits=36)
        addresses = apply_mask(mask, bin_str)
        value = int(right)
        memory |= ((address, value) for address in addresses)

print(sum(memory.values()))