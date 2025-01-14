from sympy import sympify


def parse_expression(expression):
    return sympify(expression)


print(parse_expression('2 - 1 + 4 ** 2')) # == 17
assert(parse_expression('2 - 1 + 4 ** 2') == 17) # True