def check_balanced_brackets(s):
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}
    
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
            
    return len(stack) == 0

print(check_balanced_brackets('([]{})'))
print(check_balanced_brackets('([)]'))