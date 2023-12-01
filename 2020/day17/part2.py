class Grid():
    def __init__(self):
        self.cubes = {}

    def register(self, cube):
        if cube.parent != self:
            cube.parent = self
        self.cubes |= {cube.position: cube}
        return cube

    def register_from_file(self, filepath, corner_coord=None):
        with open(filepath, "r") as f:
            cells = [line.strip("\n") for line in f]
            rows = len(cells)
            cols = len(cells[0])
            if corner_coord is None:
                start_row = -(rows // 2)
                start_col = -(cols // 2)
                start_layer = 0
                start_time = 0
            else:
                start_row, start_col, start_layer, start_time = corner_coord
            
            for y_i, row in enumerate(cells):
                for x_i, cell in enumerate(row):
                    position = (x_i + start_col, y_i + start_row, start_layer, start_time)
                    self.register(Cube(cell, position, parent=self))

    def get_adjoining(self, position):
        x, y, z, w = position
        positions = [(x_i, y_i, z_i, w_i) for x_i in [x-1, x, x+1] for y_i in [y-1, y, y+1] for z_i in [z-1, z, z+1] for w_i in [w-1, w, w+1] if (x_i, y_i, z_i, w_i) != (x, y, z, w)]
        cubes = tuple(map(self.cubes.get, positions))
        return cubes

    def advance(self, iterations):
        for _ in range(iterations):
            self.expand()
            generation = tuple(self.cubes.values())
            for cube in generation:
                cube.assess()
            for cube in generation:
                cube.update()

    def expand(self):
        max_dims = [max(el)+2 for el in zip(*self.cubes.keys())]
        min_dims = [min(el)-1 for el in zip(*self.cubes.keys())]
        x_bound, y_bound, z_bound, w_bound = tuple(zip(min_dims, max_dims))
        _ = [self.register(Cube(".", (x_i, y_i, z_i, w_i), parent=self)) for x_i in range(*x_bound) for y_i in range(*y_bound) for z_i in range(*z_bound) for w_i in range(*w_bound) if (x_i, y_i, z_i, w_i) not in self.cubes]

    def get_active_cubes(self):
        return sum(1 for cube in self.cubes.values() if cube.active)

class Cube():
    def __init__(self, state, position, parent=None):
        self.active = True if state == "#" else False
        self.position = position
        self.parent = parent
        self.toggling = False
        if type(parent) == Grid:
            parent.register(self)

    def __repr__(self):
        return "#" if self.active else "."

    def assess(self):
        active_neighbours = self.get_active_neighbour_count()
        if self.active and not (active_neighbours == 2 or active_neighbours == 3):
            self.toggling = True
        elif not self.active and active_neighbours == 3:
            self.toggling = True
        return self.toggling

    def get_active_neighbour_count(self):
        if self.parent is None or type(self.parent) != Grid:
            raise RuntimeError("You must register this cube with a grid before attempting to find its neighbours!")
        else:
            neighbours = tuple(self.parent.get_adjoining(self.position))
            active_neighbours = sum(1 for neighbour in neighbours if neighbour is not None and neighbour.active)
            return active_neighbours

    def update(self):
        if self.toggling:
            self.active = not self.active
            self.toggling = False

world = Grid()
world.register_from_file("day17/input.txt")
world.advance(6)
print(world.get_active_cubes())