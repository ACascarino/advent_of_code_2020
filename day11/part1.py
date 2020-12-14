def check(cell, row_id):
    col_id, cell_type = cell
    changed = False
    if cell_type == '#':
        pass
    elif cell_type == 'L':
        pass
    else:
        pass
    return changed

def evolve(lobby_row):
    row_id, row = lobby_row
    if any(map(lambda x: check(x, row_id), enumerate(row))) == True:
        return True
    else:
        return False

with open("day11/input.txt", "r") as f:
    initial_layout = ["." + row.rstrip('\n') + "." for row in f.readlines()]

    lobby_width = len(initial_layout[0])
    lobby_height = len(initial_layout)

    initial_layout.insert(0, "." * lobby_width)
    initial_layout.append("." * lobby_width)

layout = initial_layout
changed = True
while changed:
    changed = False

    if any(map(evolve, enumerate(layout))) == True:
        changed == True