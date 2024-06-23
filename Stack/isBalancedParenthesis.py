def isBalanced(expression):
    stack = []
    for i in expression:
        if i == '[':
            stack.append(i)
        elif i == '{':
            stack.append(i)
        elif i == '(':
            stack.append(i)
        elif i == ')':
            if len(stack) != 0:
                element = stack.pop()
                if element != '(':
                    return False
        elif i == '}':
            if len(stack) != 0:
                element = stack.pop()
                if element != '{':
                    return False
        elif i == ']':
            if len(stack) != 0:
                element = stack.pop()
                if element != '[':
                    return False

        if len(stack) == 0:
            return True


str = "[()]"
print(isBalanced(str))
