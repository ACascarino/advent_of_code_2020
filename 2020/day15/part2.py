with open("day15/input.txt", "r") as f:
    numbers = [int(n) for n in f.readline().rstrip("\n").split(",")]

counter = {n:i for i,n in enumerate(numbers[:-1])}
start_index = len(numbers)
prev_number = numbers[-1]

for i in range(start_index, 30000000):
    new_number = (i-1) - counter.get(prev_number, i-1)
    counter[prev_number] = i-1
    prev_number = new_number

print(new_number)