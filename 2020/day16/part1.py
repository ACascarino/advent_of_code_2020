with open("day16/input.txt", "r") as f:
    rules, my_ticket, other_tickets = f.read().split("\n\n")
    rules = [rule.split(": ") for rule in rules.split("\n")]
    my_ticket = my_ticket.split("\n")[1].split(",")
    other_tickets = [ticket.split(",") for ticket in other_tickets.split("\n")[1:]]

acceptable_values = set()
for label, values in rules:
    value_bounds = [tuple(value.split("-")) for value in values.split(" or ")]
    rule_values = [set(range(int(bounds[0]), int(bounds[1])+1)) for bounds in value_bounds]
    acceptable_values = acceptable_values.union(*rule_values)

error_values = []
for ticket in other_tickets:
    ticket = list(map(int, ticket))
    if (errors := [x for x in ticket if x not in acceptable_values]):
        error_values.append(*errors)

print(sum(error_values))