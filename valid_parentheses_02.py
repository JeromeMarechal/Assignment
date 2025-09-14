
def isValid(s: str) -> bool:
    opens = ['(', '[', '{']
    closes = [')', ']', '}']
    stack = []

    for char in s:
        if char in opens:
            stack.append(char)
        elif char in closes:
            if not stack:
                return False
            elif opens.index(stack[-1]) != closes.index(char):
                return False
            else:
                stack.pop()
        elif char not in opens and char not in closes:
            return False
    return not stack        
            
print(isValid("()[]{}"))   #" True"
print(isValid("(]"))        #" False" 
print(isValid("][)]"))     #" False"
        