with open("day16/input.txt", "r") as f:
    rules, my_ticket, other_tickets = f.read().split("\n\n")
    rules = [rule.split(": ") for rule in rules.split("\n")]
    my_ticket = [int(field) for field in my_ticket.split("\n")[1].split(",")]
    other_tickets = [ticket.split(",") for ticket in other_tickets.split("\n")[1:]]

acceptable_values = set()
fields = []
for label, values in rules:
    value_bounds = [tuple(value.split("-")) for value in values.split(" or ")]
    rule_values = [set(range(int(bounds[0]), int(bounds[1])+1)) for bounds in value_bounds]
    acceptable_values = acceptable_values.union(*rule_values)
    fields += [{"label": label, "values": rule_values[0].union(*rule_values)}]

valid_tickets = [set() for i in range(len(fields))]
for ticket in other_tickets:
    ticket = list(map(int, ticket))
    if any([True for x in ticket if x not in acceptable_values]):
        continue
    for i, value in enumerate(ticket):
        valid_tickets[i].add(value)

appropriate_columns = [{field['label'] for field in fields if field['values'] >= ticket_field} for ticket_field in valid_tickets]

solved_fields = set()
while not len(solved_fields) == 20:
    for i, possibilities in enumerate(appropriate_columns):
        if len(possibilities) == 1:
            solved_fields |= possibilities
        else:
            appropriate_columns[i] = possibilities - solved_fields

cumulative_product = 1
for i, field in enumerate(my_ticket):
    if appropriate_columns[i].pop().startswith("departure"):
        cumulative_product *= field

print(cumulative_product)