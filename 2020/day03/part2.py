import numpy as np

RIGHT = (1,3,5,7,1)
DOWN = (1,1,1,1,2)

def check_trees(right, down):
    with open("day03/input.txt", "r") as f:
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
    result = []
    
    for input_set in zip(RIGHT, DOWN):
        result.append(check_trees(*input_set))

    product = 1
    for elem in result:
        product *= elem
    print(product)