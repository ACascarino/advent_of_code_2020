import numpy as np

RIGHT = 1
DOWN = 3

def check_trees(right, down):
    with open("day3/input.txt", "r") as f:
        forest_tile = f.readlines()

    forest_height = len(forest_tile)
    forest_width = len(forest_tile[0].strip())

    target_width = (right / down) * forest_height

    repetitions = int(target_width // forest_width + 1)
    forest = [row.strip() * repetitions for row in forest_tile]

    row = 0
    col = 0
    counter = 0

    while row < forest_height:
        if forest[row][col] == '#':
            counter += 1
        row += down
        col += right

    return(counter)

if __name__ == "__main__":
    result = check_trees(RIGHT, DOWN)
    print(result)