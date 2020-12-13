mapping = {"F":"0", "B":"1", "L":"0", "R":"1"}
translator = "FBLR".maketrans(mapping)

with open('day5/input.txt', 'r') as f:
    rows = map(lambda x: x.translate(translator), f.readlines())

seat_ids = map(lambda x: int(x, 2), rows)
print(max(seat_ids))