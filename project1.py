import random

OPERATORS  = ["+", "-", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 12    

def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expression = str(left) + " " + str(operator) + " " + str(right)
    
    #eval() evaluates a string as if it was a python expression
    answer = eval(expression)
    return expression, answer

expression, answer = generate_problem()
print(expression, answer)