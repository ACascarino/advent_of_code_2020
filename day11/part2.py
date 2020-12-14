UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)
UP_RIGHT = (-1, 1)
UP_LEFT = (-1, -1)
DOWN_RIGHT = (1, 1)
DOWN_LEFT = (1, -1)
DIRECTIONS = (UP, UP_RIGHT, RIGHT, DOWN_RIGHT, DOWN, DOWN_LEFT, LEFT, UP_LEFT)

def transform_cell(cell, layout):
    reduced_octet = [find_nearest_seat(cell, layout, direction) for direction in DIRECTIONS]
    change = determine_change(cell, reduced_octet)
    return change

def find_nearest_seat(cell, layout, direction):
    i_row, i_col, _ = cell
    off_row, off_col = direction
    character = "."

    while character == ".":
        i_row += off_row
        i_col += off_col
        
        if i_row >= 0 and i_col >= 0:
            try:
                character = layout[i_row][i_col]
            except IndexError:
                character = "-"
        else:
            character = "-"
    return character

def determine_change(cell, octet):
    _, _, character = cell
    if character == '#' and octet.count('#') >= 5:
        change = "L"
    elif character == 'L' and octet.count('#') == 0:
        change = "#"
    else:
        change = character
    return change

with open("day11/input.txt", "r") as f:
    new_layout = [row.rstrip('\n') for row in f.readlines()]
    lobby_height = len(new_layout)
    lobby_width = len(new_layout[0])

while True:
    old_layout = new_layout.copy()
    new_layout = [[None for i in range(lobby_width)] for j in range(lobby_height)]

    for i_row, row in enumerate(old_layout):
        for i_col, character in enumerate(row):
            new_cell = transform_cell((i_row, i_col, character), old_layout)
            new_layout[i_row][i_col] = new_cell

    new_layout = ["".join(row) for row in new_layout]
    if new_layout == old_layout:
        break

print(sum(x.count('#') for x in new_layout))