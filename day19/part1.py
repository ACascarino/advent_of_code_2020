def parse(ruleset, target):
    rule = ruleset[target]
    
    if type(rule) == str:
        # type 1 - return a char
        return rule
    else:
        # type 2 or 3
        # if it's type 2, it's "or", if it's type 3, it's "and"
        if any([True for x in rule if type(x) == list]):
            #type 2 - return a frozenset of all parsed possibilities
            accumulator = []
            for content in rule:
                accumulator.append(tuple(parse(ruleset, subcontent) for subcontent in content))
            return frozenset(accumulator)
        else:
            #type 3 - return a tuple of all parsed subrules
            return tuple(parse(ruleset, content) for content in rule)

def consume(specification, testcase):
    matches = True
    token_len = 0

    for element in specification:
        shard = testcase[token_len:]
        if type(element) == str:
            matches = shard.startswith(element)
            token_len += len(element)
        elif type(element) == frozenset:
            elem_checks = [consume(subspecification, shard) for subspecification in element]
            match_vector, length_vector = list(zip(*elem_checks))
            if (true_count := match_vector.count(True)) > 0:
                if true_count > 1:
                    print("This terrible assumption does not hold")
                token_len += length_vector[match_vector.index(True)]
            else:
                matches = False
        elif type(element) == tuple:
            elem_checks = [consume(subspecification, shard) for subspecification in element]
            match_vector, length_vector = list(zip(*elem_checks))

            if all(match_vector):
                token_len += sum(length_vector)
            else:
                matches = False

        if not matches:
            break

    return (matches, token_len)

with open("day19/input.txt", "r") as f:
    rules, cases = [x.splitlines() for x in f.read().split("\n\n")]

ruleset = dict()

for rule in rules:
    rule_id, rule_contents = rule.split(": ")

    if '"' in rule_contents:
        # this means that the content is a literal, i.e. '"a"' or '"b"'
        # there are no mixed literal/nonliteral rules
        # rule_contents ends up a character e.g. 'a'
        # type 1
        rule_contents = rule_contents[1]
    elif '|' in rule_contents:
        # this means that the content is split, i.e. 18 14 | 7 12
        # rule_contents ends up a list of lists of number strings e.g. [["18", "14"], ["7", "12"]]
        # type 2
        rule_contents = [option.split(" ") for option in rule_contents.split(" | ")]
    else:
        # this means that the content is bare i.e. 12 2 4
        # rule_contents ends up a list of number strings e.g. ["12", "2", "4"]
        # type 3
        rule_contents = rule_contents.split(" ")

    ruleset |= {rule_id: rule_contents}

parsed_ruleset = parse(ruleset, "0")
counter = 0
for testcase in cases:
    matched, token_len = consume(parsed_ruleset, testcase)
    counter += 1 if matched and token_len == len(testcase) else 0
print(counter)