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

grid = HexGrid()
grid.import_from_file("day24/input.txt")
black_tiles = grid.count_black()

print(black_tiles)