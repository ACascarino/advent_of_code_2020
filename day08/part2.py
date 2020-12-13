import time

print(time.time())

with open("day08/input.txt") as f:
    assembly = f.readlines()

def check_route(assembly: list[str], modification: dict):
    pc = 0
    accumulator = 0
    seen = []

    while True:
        
        if pc == len(assembly):
            return accumulator

        current_line = assembly[pc]

        command, value = current_line.split(" ")
        value = int(value)
        increment = 1

        if modification is not None:
            if pc == modification['pc']:
                command = modification['command']
        if (pc, command) in seen:
            return seen

        if command == "acc":
            accumulator += value
        elif command == "jmp":
            increment = value

        seen.append((pc, command))
        pc += increment

first_run = check_route(assembly, None)
points_to_change = filter(lambda x: x[1] == 'jmp' or x[1] == 'nop', first_run)

while True:
    candidate = next(points_to_change)
    if candidate[1] == "jmp":
        modification = {'pc':candidate[0], 'command':"nop"}
    else:
        modification = {'pc':candidate[0], 'command':"jmp"}
    trial = check_route(assembly, modification)

    if type(trial) == int:
        print(trial)
        break

print(time.time())