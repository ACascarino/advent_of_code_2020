def expand_ruleset(ruleset, identifier):
    specs = ruleset[identifier]
    if len(specs) == 1 and '"' in specs[0][0]:
        return specs[0][0][1]
    else:
        return [[expand_ruleset(ruleset, ident) for ident in spec] for spec in specs]

def collapse_specification(specification):
    if any([True for x in specification if type(x) == list]):
        return [collapse_specification(x) if type(x) == list else x for x in specification]
    else:
        return "".join(specification)

def check_string(case, specification):
    str_pos = 0
    for subspec in specification:
        substring = case[str_pos:]
        result, offset = match_spec(substring, subspec)
        if not result:
            return False
        else:
            str_pos += offset
        if str_pos == len(case):
            return True

def match_spec(substring, subspec):
    result, offset = False, 0
    if type(subspec) == str:
        if substring.startswith(subspec):
            result = True
            offset = len(subspec)
    elif type(subspec) == list:
        if any([True for x in subspec if type(x) == list]):
            sub_matches = tuple(zip(*[match_spec(substring, sub_subspec) for sub_subspec in subspec]))
            result = any(sub_matches[0])
            offset = sum(sub_matches[1])
        else:
            if any(matched := [x for x in subspec if substring.startswith(x)]):
                result = True
                offset = len(matched[0])
    return (result, offset)
    
       
with open("day19/input.txt", "r") as f:
    rules, tests = f.read().split("\n\n")

ruleset = dict()
for rule in rules.splitlines():
    identifier, specs = rule.split(": ")
    subspecs = [spec.split(" ") for spec in specs.split(" | ")]
    ruleset |= {identifier:subspecs}

print(ruleset)
subsituted_ruleset = expand_ruleset(ruleset, identifier="0")
print(subsituted_ruleset)
string_specification = collapse_specification(subsituted_ruleset)[0]
print(string_specification)

result = sum([check_string(case, string_specification) for case in tests.splitlines()])
print(result)