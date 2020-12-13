def find_containers(rules, list_of_interesting_bags, bag_of_interest):
    list_of_interesting_bags += [rule['colour'] for rule in rules if bag_of_interest in rule['contents'].keys()]
    return list_of_interesting_bags

with open("day7/input.txt", "r") as f:
    rules = [rule.rstrip(".\n") for rule in f]

str_rules = [rule.partition(" contain ") for rule in rules]

rules = []
for rule in str_rules:
    outer_colour = rule[0].removesuffix(" bags")

    contents = rule[2].split(", ")
    if len(contents) == 1 and not contents[0][0].isdecimal:
        contains = None
    else:
        contains = dict()
        for content in contents:
            quantity = content[0]
            colour = content[2:].removesuffix("s").removesuffix(" bag")
            contains.update({colour:quantity})
    
    rules.append({"colour":outer_colour, "contents":contains})

list_of_interesting_bags = ["shiny gold"]
set_of_all_bags = set()

while list_of_interesting_bags:
    bag_of_interest = list_of_interesting_bags.pop()
    set_of_all_bags = set_of_all_bags.union(find_containers(rules, list_of_interesting_bags, bag_of_interest))

print(len(set_of_all_bags))

