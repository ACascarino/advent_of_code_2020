with open("day08/input.txt") as f:
    assembly = f.readlines()

pc = 0
accumulator = 0
seen = set()

while pc not in seen:
    current_line = assembly[pc]

    command, value = current_line.split(" ")
    value = int(value)
    increment = 1

    if command == "acc":
        accumulator += value
    elif command == "jmp":
        increment = value

    seen.add(pc)
    pc += increment

print(accumulator)