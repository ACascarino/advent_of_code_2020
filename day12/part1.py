class Vector(tuple):
    def __add__(self, a):
        return Vector(x + y for x,y in zip(self, a))
    def __mul__(self, c):
        return Vector(x * c for x in self)
    def __rmul__(self, c):
        return Vector(c * x for x in self)

    def pivot(self, direction):
        if direction > 0:
            return Vector((self[1], -self[0]))
        if direction < 0:
            return Vector((-self[1], self[0]))

    def manhatten(self):
        return abs(sum(self))

def move(position, direction, value):
    offset = direction * value
    position += offset
    return position

def pivot(heading, direction, value):
    offset = (direction * value) // 90
    heading += offset
    return (heading % 4)

STARTING_POSITION = Vector((0, 0))

NORTH = Vector((-1, 0))
EAST = Vector((0, 1))
SOUTH = Vector((1, 0))
WEST = Vector((0, -1))
DIRECTIONS = [NORTH, EAST, SOUTH, WEST]

LEFT = -1
RIGHT = 1

STARTING_HEADING = 1

with open("day12/input.txt", "r") as f:
    bearings = [b.rstrip("\n") for b in f]

position = STARTING_POSITION
heading = STARTING_HEADING

for bearing in bearings:
    value = int(bearing[1:])
    if bearing.startswith("N"):
        position = move(position, NORTH, value)
    elif bearing.startswith("E"):
        position = move(position, EAST, value)
    elif bearing.startswith("S"):
        position = move(position, SOUTH, value)
    elif bearing.startswith("W"):
        position = move(position, WEST, value)
    elif bearing.startswith("F"):
        position = move(position, DIRECTIONS[heading], value)
    elif bearing.startswith("L"):
        heading = pivot(heading, LEFT, value)
    elif bearing.startswith("R"):
        heading = pivot(heading, RIGHT, value)

print(position.manhatten())