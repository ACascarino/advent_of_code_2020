import numpy as np

with open("day2/input.txt", "r") as f:
    input_file = [tuple(l.split()) for l in f.readlines()]

for entry in input_file:
    schema, letter, password = entry
    
    lowbound, highbound = schema.split('-')
    letter = letter[0]