NORTH = 0
EAST = 90
SOUTH = 180
WEST = 270
DIRECTIONS = {NORTH: (0, 1), EAST: (1, 0), SOUTH: (0, -1), WEST: (-1, 0)}

def add_tuples(tup1, tup2):
    if type(tup2) == tuple:
        if len(tup1) != len(tup2):
            raise ValueError
        else:
            return tuple(tup1[i] + tup2[i] for i in range(len(tup1)))
    elif type(tup2) == list:
        return tuple(add_tuples(tup1, in_tup) for in_tup in tup2)

def string_comp(str1, str2):
    if len(str1) != len(str2):
        raise ValueError
    
    result = [char1 == char2 for char1, char2 in zip(str1, str2) if char1 is not None and char2 is not None]
    
    return all(result)

class Board():
    def __init__(self):
        self.tiles = []
        self.arrangement = dict()

    def register(self, registrant):
        self.tiles.append(registrant)
        if registrant.parent is None:
            registrant.parent = self

    def register_from_file(self, filepath):
        with open(filepath, "r") as f:
            tiles = [tile.split("\n") for tile in f.read().split("\n\n")]

        for tile in tiles:
            tile_id = tile[0].strip("Tile :")
            tile_body = tile[1:]
            self.register(Tile(tile_id, tile_body))

    def import_monster(self, filepath):
        with open(filepath, "r") as f:
            self.monster = [[x if x != " " else None for x in row.strip("\n")] for row in f]
            self.monster_height = len(self.monster)
            self.monster_width = len(self.monster[0])

    def pair_tiles(self):
        starting_tile = self.tiles[0]
        starting_coords = (0, 0)
        starting_tile.placed = True
        self.arrangement |= {starting_coords:starting_tile}

        stack = [(starting_coords, starting_tile)]
        while stack:
            coords, tile = stack.pop()
            for other in self.tiles:
                if other == tile or other.placed:
                    continue
                if (direction := tile.check(other)) is not None:
                    other.placed = True
                    new_coords = add_tuples(coords, DIRECTIONS[direction])
                    self.arrangement |= {new_coords:other}
                    stack.append((new_coords,other))

    def get_extrema(self):
        x,y = tuple(zip(*self.arrangement))
        return [(min(x), max(x)), (min(y), max(y))]

    def get_corners(self):
        (min_x, max_x), (min_y, max_y) = self.get_extrema()
        bounds = ((min_x, min_y), (min_x, max_y), (max_x, min_y), (max_x, max_y))
        return [self.arrangement[corner] for corner in bounds]

    def generate_render(self):
        (min_x, max_x), (min_y, max_y) = self.get_extrema()
        range_x = max_x - min_x
        range_y = max_y - min_y

        canvas = [[None] * (range_x + 1) for y in range(range_y + 1)]
        for (x,y),tile in self.arrangement.items():
            body = tile.body 
            contents = [row[1:-1] for row in body[1:-1]]
            canvas[max_y-y][x-min_x] = contents
        self.render = ["".join(subrow) for row in canvas for subrow in list(zip(*row))]

    def rot90_render(self, rotations):
        for _ in range(rotations):
            self.render = ["".join(row) for row in zip(*self.render[::-1])]
    
    def flipX_render(self):
        self.render = self.render[::-1]

    def flipY_render(self):
        self.render = [row[::-1] for row in self.render]

    def count_monsters(self):
        monster_count = 0
        cycling = True
        rotations = 0
        flipped = False

        while cycling:
            for i,row in enumerate(self.render[:-self.monster_height+1]):
                monster_col = []
                for j in range((len(row) - self.monster_width) + 1):
                    segment = row[j:j+self.monster_width]
                    if string_comp(segment, self.monster[0]):
                        monster_col.append(j)
                if monster_col:
                    for col in monster_col:
                        monster_found = True
                        for h in range(self.monster_height):
                            segment = self.render[i+h][col:col+self.monster_width]
                            if not string_comp(segment, self.monster[h]):
                                monster_found = False
                                break
                        if monster_found:
                            monster_count += 1
            
            if monster_count == 0:
                self.rot90_render(1)
                rotations += 1
                if rotations == 4:
                    if not flipped:
                        self.flipX_render()
                        flipped = True
                        rotations = 0
                    else:
                        rotations = 0
                        print("panic")
            else:
                cycling = False
        
        self.monster_count = monster_count

    def count_dark_spots(self):
        self.dark_spots = sum(row.count("#") for row in self.render)

    def get_roughness(self):
        monster_dark_spots = sum(row.count("#") for row in self.monster)
        return self.dark_spots - (monster_dark_spots * self.monster_count)

class Tile():
    def __init__(self, in_id, body):
        self.id = int(in_id)
        self.body = body
        self.parent = None
        self.edge_tiles = {NORTH:None, EAST:None, SOUTH:None, WEST:None}
        self.placed = False

        self.generate_edges()

    def __repr__(self):
        return str(self.id)

    def check(self, other):
        for edge, val in self.edges.items():
            match = [(other_edge, False) for other_edge, other_val in other.edges.items() if val == other_val]
            if not match:
                match = [(other_edge, True) for other_edge, other_val in other.rev_edges.items() if val == other_val]
            if not match:
                continue
            else:
                match_edge, reverse = match[0]

                self.edge_tiles[edge] = other
                other.edge_tiles[match_edge] = self
                
                rotations = (((edge - match_edge) + 180) % 360) // 90
                flip_y = True if not reverse and (match_edge == NORTH or match_edge == SOUTH) else False
                flip_x = True if not reverse and (match_edge == WEST or match_edge == EAST) else False

                if flip_y:
                    other.flipY()
                if flip_x:
                    other.flipX()

                other.rot90(rotations)

                return edge
        return None

    def get_dirs(self, directions):
        return tuple(self.edge_tiles[direction] for direction in directions)

    def rot90(self, rotations):
        for _ in range(rotations):
            self.body = ["".join(row) for row in zip(*self.body[::-1])]
        self.edge_tiles = {(direction + 90*rotations) % 360:value for direction, value in self.edge_tiles.items()}
        self.generate_edges()

    def flipX(self):
        self.body = self.body[::-1]
        self.edge_tiles[NORTH], self.edge_tiles[SOUTH] = self.edge_tiles[SOUTH], self.edge_tiles[NORTH]
        self.generate_edges()

    def flipY(self):
        self.body = [row[::-1] for row in self.body]
        self.edge_tiles[WEST], self.edge_tiles[EAST] = self.edge_tiles[EAST], self.edge_tiles[WEST]
        self.generate_edges()

    def generate_edges(self):
        self.edges = {NORTH: self.body[0], 
                        EAST: "".join([line[-1] for line in self.body]), 
                        SOUTH: self.body[-1][::-1], 
                        WEST: "".join([line[0] for line in self.body])[::-1]}
        self.rev_edges = {key:value[::-1] for key,value in self.edges.items()}
                
if __name__ == "__main__":
    world = Board()
    world.register_from_file("day20/input.txt")
    world.import_monster("day20/monster.txt")
    world.pair_tiles()
    world.generate_render()
    world.count_monsters()
    world.count_dark_spots()
    print(world.get_roughness())