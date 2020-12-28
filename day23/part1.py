with open("day23/input.txt", "r") as f:
    starting_arrangement = [int(char) for char in f.read()]

ll = len(starting_arrangement)

for i in range(ll+1, 1000001):
    starting_arrangement.append(i)

ll = len(starting_arrangement)

wl = {key:starting_arrangement[i+1 if i != ll-1 else 0] for i,key in enumerate(starting_arrangement)}
sn = starting_arrangement[0]

for i in range(10000000):
    one, two, three = (wl[sn], wl[wl[sn]], wl[wl[wl[sn]]])
    next_int = ((sn-1) % ll)

    while True:
        if next_int == 0:
            next_int = ll

        if next_int in [one, two, three]:
            next_int = ((next_int - 1) % ll)
        else:
            break

    head = wl[next_int]
    wl[sn] = wl[three]
    wl[next_int] = one
    wl[three] = head

    sn = wl[sn]

start_int = 1
work_int = start_int
order = []

cup1 = wl[1]
cup2 = wl[cup1]

print(cup1 * cup2)