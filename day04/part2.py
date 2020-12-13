import numpy as np

with open("day04/input.txt", "r") as f:
    input_file = f.read()
    passport_strings = [passport.split() for passport in input_file.split("\n\n")]
    passports = [{key:val for key,val in map(lambda x: x.split(':'), passport)} for passport in passport_strings]

counter = 0
for passport in passports:
    if not {'hgt', 'iyr', 'byr', 'hcl', 'eyr', 'pid', 'ecl'} <= passport.keys():
        continue

    if not (int(passport['byr']) >= 1920 and int(passport['byr']) <= 2002):
        continue

    if not (int(passport['iyr']) >= 2010 and int(passport['iyr']) <= 2020):
        continue

    if not (int(passport['eyr']) >= 2020 and int(passport['eyr']) <= 2030):
        continue

    if passport['hgt'].endswith("cm"):
        if not (int(passport['hgt'].removesuffix("cm")) >= 150 and int(passport['hgt'].removesuffix("cm")) <= 193):
            continue
    elif passport['hgt'].endswith("in"):
        if not (int(passport['hgt'].removesuffix("in")) >= 59 and int(passport['hgt'].removesuffix("in")) <= 76):
            continue
    else:
        continue

    if passport['hcl'].startswith("#") and len(passport['hcl']) == 7:
        if not (set('0123456789abcdef') >= set(passport['hcl'][1:])):
            continue
    else:
        continue

    if passport['ecl'] not in set(("amb", "blu", "brn", "gry", "grn", "hzl", "oth")):
        continue

    if len(passport['pid']) != 9 or not passport['pid'].isdecimal():
        continue

    counter += 1

print(counter)