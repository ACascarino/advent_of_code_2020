DIVISOR = 20201227

def transform(value, subject_number):
    return (value * subject_number) % DIVISOR

def encrypt(loop_size, subject_number):
    value = 1
    for _ in range(loop_size):
        value = transform(value, subject_number)
    return value

def solve(target, starting_value, subject_number):
    loop_size = 0
    value = starting_value
    while value != target:
        loop_size += 1
        value = transform(value, subject_number)
    return loop_size
    
with open("day25/input.txt", "r") as f:
    card, door = [int(x) for x in f.read().split("\n")]

card_loop = solve(card, 1, 7)
encryption_key = encrypt(card_loop, door)

print(encryption_key)