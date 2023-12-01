def list_resolver(input_list):
    resolved_expression = "".join([list_resolver(item) if type(item) == list else item for item in input_list])
    parsed = parse(resolved_expression)
    return(parsed)

def parse(expression):
    result = 1

    operators = [elem for elem in expression if elem in ["*", "+"]]
    operands = [int(elem) for bigchunk in [chunk.split("+") for chunk in expression.split("*")] for elem in bigchunk]

    for ind, operator in enumerate(operators):
        if operator == "+":
            operands[ind+1] = operands[ind] + operands[ind+1]
            operands[ind] = 1
    
    for operand in operands:
        result *= operand

    return(str(result))

with open("day18/input.txt", "r") as f:
    expressions = [line.rstrip("\n") for line in f]

sum = 0
for expression in expressions:
    expression_parsed = eval("[\"" + expression.replace("(", "\",[\"").replace(")", "\"],\"").replace(" ", "") + "\"]")
    result = list_resolver(expression_parsed)
    sum += int(result)
print(sum)