OPERATORS = {"+":lambda x,y: x+y, "*":lambda x,y: x*y}

def list_resolver(input_list):
    resolved_expression = "".join([list_resolver(item) if type(item) == list else item for item in input_list])
    parsed = parse(resolved_expression)
    return(parsed)

def parse(expression):
    result = 0

    operators = [elem for elem in expression if elem in OPERATORS] + ["+"]
    operands = [elem for bigchunk in [chunk.split("+") for chunk in expression.split("*")] for elem in bigchunk]

    for ind, element in enumerate(operands):
        result = OPERATORS[operators[ind-1]](result, int(element))
    return str(result)

with open("day18/input.txt", "r") as f:
    expressions = [line.rstrip("\n") for line in f]

sum = 0
for expression in expressions:
    expression_parsed = eval("[\"" + expression.replace("(", "\",[\"").replace(")", "\"],\"").replace(" ", "") + "\"]")
    result = list_resolver(expression_parsed)
    sum += int(result)
print(sum)