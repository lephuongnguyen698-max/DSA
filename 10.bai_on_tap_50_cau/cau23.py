def evaluate_postfix(expression):
    stack = []
    tokens = expression.split()
    
    for token in tokens:
        if token.isdigit():
            stack.append(int(token))
        else:
            val2 = stack.pop()
            val1 = stack.pop()
            if token == '+':
                stack.append(val1 + val2)
            elif token == '-':
                stack.append(val1 - val2)
            elif token == '*':
                stack.append(val1 * val2)
            elif token == '/':
                stack.append(int(val1 / val2))
                
    return stack[0]

print(evaluate_postfix('3 4 + 2 *'))