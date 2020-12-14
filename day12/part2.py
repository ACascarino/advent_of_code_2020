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

def move_wp(position, direction, value):
    offset = direction * value
    position += offset
    return position

def move_s(s_position, w_position, value):
    offset = w_position * value
    s_position += offset
    return s_position

def pivot_wp(w_position, direction, value):
    steps = value // 90
    for _ in range(steps):
        w_position = w_position.pivot(direction)
    return w_position

SHIP_STARTING_POSITION = Vector((0, 0))
WAYPOINT_STARTING_POSITION = Vector((-1, 10))

NORTH = Vector((-1, 0))
EAST = Vector((0, 1))
SOUTH = Vector((1, 0))
WEST = Vector((0, -1))

LEFT = -1
RIGHT = 1

with open("day12/input.txt", "r") as f:
    bearings = [b.rstrip("\n") for b in f]

s_position = SHIP_STARTING_POSITION
w_position = WAYPOINT_STARTING_POSITION

for bearing in bearings:
    value = int(bearing[1:])
    if bearing.startswith("N"):
        w_position = move_wp(w_position, NORTH, value)
    elif bearing.startswith("E"):
        w_position = move_wp(w_position, EAST, value)
    elif bearing.startswith("S"):
        w_position = move_wp(w_position, SOUTH, value)
    elif bearing.startswith("W"):
        w_position = move_wp(w_position, WEST, value)
    elif bearing.startswith("F"):
        s_position = move_s(s_position, w_position, value)
    elif bearing.startswith("L"):
        w_position = pivot_wp(w_position, LEFT, value)
    elif bearing.startswith("R"):
        w_position = pivot_wp(w_position, RIGHT, value)

print(s_position.manhatten())