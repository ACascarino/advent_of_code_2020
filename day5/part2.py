mapping = {"F":"0", "B":"1", "L":"0", "R":"1"}
translator = "FBLR".maketrans(mapping)

with open('day5/input.txt', 'r') as f:
    rows = tuple(map(lambda x: x.translate(translator), f.readlines()))

row_ids = tuple(map(lambda x: int(x[:7], 2), rows))
seat_ids = set(map(lambda x: int(x, 2), rows))

max_row = max(row_ids) - 1
min_row = min(row_ids) + 1
possible_seats = set(range(min_row*8, (max_row*8)+1))
print(possible_seats - seat_ids)

