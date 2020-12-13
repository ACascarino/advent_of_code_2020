import numpy as np

with open("day4/input.txt", "r") as f:
    input_file = f.read()
    passport_strings = [passport.split() for passport in input_file.split("\n\n")]
    passports = [{key:val for key,val in map(lambda x: x.split(':'), passport)} for passport in passport_strings]

counter = 0
for passport in passports:
    if not {'hgt', 'iyr', 'byr', 'hcl', 'eyr', 'pid', 'ecl'} <= passport.keys():
        continue

    counter += 1

print(counter)