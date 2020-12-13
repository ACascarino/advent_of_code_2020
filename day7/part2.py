with open("day7/input.txt", "r") as f:
    rules = [rule.rstrip(".\n") for rule in f]

str_rules = [rule.partition(" contain ") for rule in rules]

rules = []
for rule in str_rules:
    outer_colour = rule[0].removesuffix(" bags")

    contents = rule[2].split(", ")
    if len(contents) == 1 and not contents[0][0].isdecimal():
        contains = None
    else:
        contains = dict()
        for content in contents:
            quantity = content[0]
            colour = content[2:].removesuffix("s").removesuffix(" bag")
            contains.update({colour:int(quantity)})
    
    rules.append({"colour":outer_colour, "contents":contains})

bags_of_interest = ["shiny gold"]
number_of_bags = 0

while bags_of_interest:
    bag_colour = bags_of_interest.pop()
    bag_rule = next(filter(lambda x: x['colour'] == bag_colour, rules))

    if (contents := bag_rule['contents']) is not None:

        for key,value in zip(list(contents.keys()), list(contents.values())):
            bags_of_interest += [key]*value

        number_of_bags += sum(list(contents.values()))

print(number_of_bags)