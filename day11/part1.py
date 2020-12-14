def as_group(iterable: [], grouping: int, start:int = 0, end:int = None):
    i = start
    end = end if end is not None else len(iterable)-grouping
    while i <= end:
        yield(iterable[i:i+grouping])
        i += 1

def check(cell):
    change = False
    cell_type = cell[1][1]
    if cell_type == '#':
        if sum(c.count('#') for c in cell) >= 5:
            change = ('L')
    elif cell_type == 'L':
        if not any('#' in c for c in cell):
            change = ('#')
    else:
        pass
    return change

def evolve(lobby_row):
    cols = tuple(zip(*lobby_row))
    tri_cols = as_group(cols, 3)
    changes = tuple(map(check, tri_cols))
    if any(changes) == True:
        return changes
    else:
        return False

def pad(string_set:list[str], delimiter:str):
    string_set = [delimiter + row + delimiter for row in string_set]
    width = len(string_set[0])
    string_set.insert(0, delimiter * width)
    string_set.append(delimiter * width)

    return string_set

with open("day11/input.txt", "r") as f:
    layout = [row.rstrip('\n') for row in f.readlines()]
    layout = pad(layout, ".")

changed = True
while changed:
    changed = False
    thruples = as_group(layout, 3)

    changes = tuple(map(evolve, thruples))
    if any(changes) == True:
        changed = True
        layout = ["".join([cell if cell else layout[i_row+1][i_col+1] for i_col, cell in enumerate(row)]) if row else layout[i_row+1][1:-1] for i_row, row in enumerate(changes)]
        layout = pad(layout, ".")
    print(sum(row.count("#") for row in layout))