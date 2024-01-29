def parentest(inp):
    stk=[]
    validinp="({[]})"
    for char in inp:
        if char not in validinp:
            return False
        if char=='(' or char=='{' or char=='[':
            stk.append(char)
        elif char==')' and (not stk or stk.pop()!='('):
            return False
        elif char=='}' and (not stk or stk.pop()!='{' ):
            return False
        elif char==']' and (not stk or stk.pop()!='['):
            return False
    return not stk


print(parentest("[{()}]"))
print(parentest("()[]{}"))
print(parentest("(]"))
print(parentest("{{[()]]}}"))
print(parentest("{[()]}"))
print(parentest("abc()def"))
print(parentest("()abcdef"))
print(parentest("{{[()]}}"))
