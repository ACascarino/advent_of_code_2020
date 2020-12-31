DIRECTIONS = {"e":(1, 0), "ne":(1, 1), "nw":(0, 1), "w":(-1, 0), "sw":(-1, -1), "se": (0, -1)}

def add_tuples(tup1, tup2):
    return tuple(tup1[i] + tup2[i] for i in range(len(tup1)))

class HexGrid():
    def __init__(self):
        self.tiles = dict()

    def import_from_file(self, filepath):
        with open(filepath, "r") as f:
            instructions = [line.strip("\n") for line in f]

        parsed = map(self.parse, instructions)
        self.define_grid(parsed)

    def parse(self, instruction):
        composite = None
        results = []
        for char in instruction:
            if char == "n" or char == "s":
                composite = char
                continue
            else:
                result = composite + char if composite is not None else char
                composite = None
                results.append(result)
        return results

    def define_grid(self, parsed):
        for instruction in parsed:
            e, ne, nw, w, sw, se = [instruction.count(direction) for direction in DIRECTIONS]
            a = (w - e)
            b = (nw - se)
            c = (ne - sw)
            x, y = (a+b, c+b)
            coord = (x, y)
            
            target = self.tiles.get(coord, None)
            self.tiles[coord] = target.flip() if target is not None else Tile(True)

    def advance(self, iterations):
        for _ in range(iterations):
            next_state = dict()

            for item in self.tiles.items():
                queue = [item]
                while queue:
                    coord, tile = queue.pop()
                    new_coords = [add_tuples(coord, direction) for direction in DIRECTIONS.values()]
                    neighbours = [self.tiles.get(new_coord, False) for new_coord in new_coords]
                    if tile and (False in neighbours):
                        for new_coord in new_coords:
                            if new_coord not in self.tiles:
                                new_tile = Tile(False)
                                queue.append((new_coord, new_tile))
                                next_state |= {new_coord: new_tile}
                    next_state |= {coord:tile.get_new_state(neighbours)}
            self.tiles = next_state
    
    def count_black(self):
        return sum(1 for tile in self.tiles.values() if tile)

class Tile():
    def __init__(self, is_black):
        self.is_black = is_black

    def __bool__(self):
        return self.is_black

    def flip(self):
        self.is_black = not self.is_black
        return self
    
    def copy(self):
        return Tile(self.is_black)

    def get_new_state(self, neighbours):
        black_neighbours = sum(1 for tile in neighbours if tile)
        new_tile = self

        if self.is_black:
            if black_neighbours == 0 or black_neighbours > 2:
                new_tile = self.copy().flip() 
        else:
            if black_neighbours == 2:
                new_tile = self.copy().flip()
        return new_tile

grid = HexGrid()
grid.import_from_file("day24/input.txt")
grid.advance(100)
black_tiles = grid.count_black()

print(black_tiles)